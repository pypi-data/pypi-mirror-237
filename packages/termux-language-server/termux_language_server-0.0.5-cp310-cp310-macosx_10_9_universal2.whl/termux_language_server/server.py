r"""Server
==========
"""
import re
from typing import Any

from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    TEXT_DOCUMENT_DID_CHANGE,
    TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_DOCUMENT_LINK,
    TEXT_DOCUMENT_FORMATTING,
    TEXT_DOCUMENT_HOVER,
    CompletionItem,
    CompletionItemKind,
    CompletionList,
    CompletionParams,
    DidChangeTextDocumentParams,
    DocumentFormattingParams,
    DocumentLink,
    DocumentLinkParams,
    Hover,
    MarkupContent,
    MarkupKind,
    Position,
    TextDocumentPositionParams,
    TextEdit,
)
from pygls.server import LanguageServer

from .finders import (
    DIAGNOSTICS_FINDER_CLASSES,
    FORMAT_FINDER_CLASSES,
    CSVFinder,
    PackageFinder,
)
from .parser import parse
from .tree_sitter_lsp.diagnose import get_diagnostics
from .tree_sitter_lsp.finders import PositionFinder
from .tree_sitter_lsp.format import get_text_edits
from .utils import get_filetype, get_schema


class TermuxLanguageServer(LanguageServer):
    r"""Termux language server."""

    def __init__(self, *args: Any) -> None:
        r"""Init.

        :param args:
        :type args: Any
        :rtype: None
        """
        super().__init__(*args)
        self.trees = {}

        @self.feature(TEXT_DOCUMENT_DID_OPEN)
        @self.feature(TEXT_DOCUMENT_DID_CHANGE)
        def did_change(params: DidChangeTextDocumentParams) -> None:
            r"""Did change.

            :param params:
            :type params: DidChangeTextDocumentParams
            :rtype: None
            """
            filetype = get_filetype(params.text_document.uri)
            if filetype == "":
                return None
            document = self.workspace.get_document(params.text_document.uri)
            self.trees[document.uri] = parse(document.source.encode())
            diagnostics = get_diagnostics(
                document.uri,
                self.trees[document.uri],
                DIAGNOSTICS_FINDER_CLASSES,
                filetype,
            )
            self.publish_diagnostics(params.text_document.uri, diagnostics)

        @self.feature(TEXT_DOCUMENT_FORMATTING)
        def format(params: DocumentFormattingParams) -> list[TextEdit]:
            r"""Format.

            :param params:
            :type params: DocumentFormattingParams
            :rtype: list[TextEdit]
            """
            filetype = get_filetype(params.text_document.uri)
            if filetype == "":
                return []
            document = self.workspace.get_document(params.text_document.uri)
            return get_text_edits(
                document.uri,
                self.trees[document.uri],
                FORMAT_FINDER_CLASSES,
                filetype,
            )

        @self.feature(TEXT_DOCUMENT_DOCUMENT_LINK)
        def document_link(params: DocumentLinkParams) -> list[DocumentLink]:
            r"""Get document links.

            :param params:
            :type params: DocumentLinkParams
            :rtype: list[DocumentLink]
            """
            filetype = get_filetype(params.text_document.uri)
            if filetype == "":
                return []
            document = self.workspace.get_document(params.text_document.uri)
            if filetype in {"build.sh", "subpackage.sh"}:
                return CSVFinder(filetype).get_document_links(
                    document.uri,
                    self.trees[document.uri],
                    "https://github.com/termux/termux-packages/tree/master/packages/{{name}}/build.sh",
                )
            elif filetype in {"PKGBUILD", "install"}:
                return PackageFinder().get_document_links(
                    document.uri,
                    self.trees[document.uri],
                    "https://archlinux.org/packages/{{uni.get_text()}}",
                )
            raise NotImplementedError

        @self.feature(TEXT_DOCUMENT_HOVER)
        def hover(params: TextDocumentPositionParams) -> Hover | None:
            r"""Hover.

            :param params:
            :type params: TextDocumentPositionParams
            :rtype: Hover | None
            """
            filetype = get_filetype(params.text_document.uri)
            if filetype == "":
                return None
            document = self.workspace.get_document(params.text_document.uri)
            uni = PositionFinder(params.position).find(
                document.uri, self.trees[document.uri]
            )
            if uni is None:
                return None
            parent = uni.node.parent
            # we only hover variable names and function names
            if parent is None or not (
                uni.node.type == "variable_name"
                or uni.node.type == "word"
                and parent.type
                in {
                    "function_definition",
                    "command_name",
                }
            ):
                return None
            text = uni.get_text()
            _range = uni.get_range()
            if description := (
                get_schema(filetype)
                .get("properties", {})
                .get(text, {})
                .get("description")
            ):
                return Hover(
                    MarkupContent(MarkupKind.Markdown, description),
                    _range,
                )
            for k, v in (
                get_schema(filetype).get("patternProperties", {}).items()
            ):
                if re.match(k, text):
                    return Hover(
                        MarkupContent(MarkupKind.Markdown, v["description"]),
                        _range,
                    )

        @self.feature(TEXT_DOCUMENT_COMPLETION)
        def completions(params: CompletionParams) -> CompletionList:
            r"""Completions.

            :param params:
            :type params: CompletionParams
            :rtype: CompletionList
            """
            filetype = get_filetype(params.text_document.uri)
            if filetype == "":
                return CompletionList(False, [])
            document = self.workspace.get_document(params.text_document.uri)
            uni = PositionFinder(
                Position(params.position.line, params.position.character - 1)
            ).find(document.uri, self.trees[document.uri])
            if uni is None:
                return CompletionList(False, [])
            text = uni.get_text()
            schema = get_schema(filetype)
            return CompletionList(
                False,
                [
                    CompletionItem(
                        k,
                        kind=CompletionItemKind.Function
                        if v.get("const") == 0
                        else CompletionItemKind.Field
                        if v.get("type") == "array"
                        else CompletionItemKind.Variable,
                        documentation=MarkupContent(
                            MarkupKind.Markdown, v["description"]
                        ),
                        insert_text=k,
                    )
                    for k, v in (
                        schema.get("properties", {})
                        | {
                            k.lstrip("^").split("(")[0]: v
                            for k, v in schema.get(
                                "patternProperties", {}
                            ).items()
                        }
                    ).items()
                    if k.startswith(text)
                ],
            )
