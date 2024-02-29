"""Node parsers."""

from lyzr_rag.node_parser.file.html import HTMLNodeParser
from lyzr_rag.node_parser.file.json import JSONNodeParser
from lyzr_rag.node_parser.file.markdown import MarkdownNodeParser
from lyzr_rag.node_parser.file.simple_file import SimpleFileNodeParser
from lyzr_rag.node_parser.interface import (
    MetadataAwareTextSplitter,
    NodeParser,
    TextSplitter,
)
from lyzr_rag.node_parser.relational.hierarchical import (
    HierarchicalNodeParser,
    get_leaf_nodes,
    get_root_nodes,
)
from lyzr_rag.node_parser.relational.markdown_element import (
    MarkdownElementNodeParser,
)
from lyzr_rag.node_parser.relational.unstructured_element import (
    UnstructuredElementNodeParser,
)
from lyzr_rag.node_parser.text.code import CodeSplitter
from lyzr_rag.node_parser.text.langchain import LangchainNodeParser
from lyzr_rag.node_parser.text.semantic_splitter import SemanticSplitterNodeParser
from lyzr_rag.node_parser.text.sentence import SentenceSplitter
from lyzr_rag.node_parser.text.sentence_window import SentenceWindowNodeParser
from lyzr_rag.node_parser.text.token import TokenTextSplitter

# deprecated, for backwards compatibility
SimpleNodeParser = SentenceSplitter

__all__ = [
    "TokenTextSplitter",
    "SentenceSplitter",
    "CodeSplitter",
    "SimpleFileNodeParser",
    "HTMLNodeParser",
    "MarkdownNodeParser",
    "JSONNodeParser",
    "SentenceWindowNodeParser",
    "SemanticSplitterNodeParser",
    "NodeParser",
    "HierarchicalNodeParser",
    "TextSplitter",
    "MarkdownElementNodeParser",
    "MetadataAwareTextSplitter",
    "LangchainNodeParser",
    "UnstructuredElementNodeParser",
    "get_leaf_nodes",
    "get_root_nodes",
    # deprecated, for backwards compatibility
    "SimpleNodeParser",
]
