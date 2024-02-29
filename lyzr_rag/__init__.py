"""Init file of LlamaIndex."""

from pathlib import Path

with open(Path(__file__).absolute().parents[0] / "VERSION") as _f:
    __version__ = _f.read().strip()


import logging
from logging import NullHandler
from typing import Callable, Optional

# import global eval handler
from lyzr_rag.callbacks.global_handlers import set_global_handler

# response
from lyzr_rag.core.response.schema import Response
from lyzr_rag.data_structs.struct_type import IndexStructType

# embeddings
from lyzr_rag.embeddings import OpenAIEmbedding

# indices
# loading
from lyzr_rag.indices import (
    ComposableGraph,
    DocumentSummaryIndex,
    GPTDocumentSummaryIndex,
    GPTKeywordTableIndex,
    GPTKnowledgeGraphIndex,
    GPTListIndex,
    GPTRAKEKeywordTableIndex,
    GPTSimpleKeywordTableIndex,
    GPTTreeIndex,
    GPTVectorStoreIndex,
    KeywordTableIndex,
    KnowledgeGraphIndex,
    ListIndex,
    RAKEKeywordTableIndex,
    SimpleKeywordTableIndex,
    SummaryIndex,
    TreeIndex,
    VectorStoreIndex,
    load_graph_from_storage,
    load_index_from_storage,
    load_indices_from_storage,
)

# structured
from lyzr_rag.indices.common.struct_store.base import SQLDocumentContextBuilder

# prompt helper
from lyzr_rag.indices.prompt_helper import PromptHelper
from lyzr_rag.llm_predictor import LLMPredictor

# token predictor
from lyzr_rag.llm_predictor.mock import MockLLMPredictor

# prompts
from lyzr_rag.prompts import (
    BasePromptTemplate,
    ChatPromptTemplate,
    # backwards compatibility
    Prompt,
    PromptTemplate,
    SelectorPromptTemplate,
)
from lyzr_rag.readers import (
    SimpleDirectoryReader,
    download_loader,
)

# Response Synthesizer
from lyzr_rag.response_synthesizers.factory import get_response_synthesizer
from lyzr_rag.schema import Document, QueryBundle
from lyzr_rag.service_context import (
    ServiceContext,
    set_global_service_context,
)

# storage
from lyzr_rag.storage.storage_context import StorageContext
from lyzr_rag.token_counter.mock_embed_model import MockEmbedding

# sql wrapper
from lyzr_rag.utilities.sql_wrapper import SQLDatabase

# global tokenizer
from lyzr_rag.utils import get_tokenizer, set_global_tokenizer

# best practices for library logging:
# https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
logging.getLogger(__name__).addHandler(NullHandler())

__all__ = [
    "StorageContext",
    "ServiceContext",
    "ComposableGraph",
    # indices
    "SummaryIndex",
    "VectorStoreIndex",
    "SimpleKeywordTableIndex",
    "KeywordTableIndex",
    "RAKEKeywordTableIndex",
    "TreeIndex",
    "DocumentSummaryIndex",
    "KnowledgeGraphIndex",
    # indices - legacy names
    "GPTKeywordTableIndex",
    "GPTKnowledgeGraphIndex",
    "GPTSimpleKeywordTableIndex",
    "GPTRAKEKeywordTableIndex",
    "GPTListIndex",
    "ListIndex",
    "GPTTreeIndex",
    "GPTVectorStoreIndex",
    "GPTDocumentSummaryIndex",
    "Prompt",
    "PromptTemplate",
    "BasePromptTemplate",
    "ChatPromptTemplate",
    "SelectorPromptTemplate",
    "OpenAIEmbedding",
    "SummaryPrompt",
    "TreeInsertPrompt",
    "TreeSelectPrompt",
    "TreeSelectMultiplePrompt",
    "RefinePrompt",
    "QuestionAnswerPrompt",
    "KeywordExtractPrompt",
    "QueryKeywordExtractPrompt",
    "Response",
    "Document",
    "SimpleDirectoryReader",
    "LLMPredictor",
    "MockLLMPredictor",
    "VellumPredictor",
    "VellumPromptRegistry",
    "MockEmbedding",
    "SQLDatabase",
    "SQLDocumentContextBuilder",
    "SQLContextBuilder",
    "PromptHelper",
    "IndexStructType",
    "download_loader",
    "load_graph_from_storage",
    "load_index_from_storage",
    "load_indices_from_storage",
    "QueryBundle",
    "get_response_synthesizer",
    "set_global_service_context",
    "set_global_handler",
    "set_global_tokenizer",
    "get_tokenizer",
]

# eval global toggle
from lyzr_rag.callbacks.base_handler import BaseCallbackHandler

global_handler: Optional[BaseCallbackHandler] = None

# NOTE: keep for backwards compatibility
SQLContextBuilder = SQLDocumentContextBuilder

# global service context for ServiceContext.from_defaults()
global_service_context: Optional[ServiceContext] = None

# global tokenizer
global_tokenizer: Optional[Callable[[str], list]] = None
