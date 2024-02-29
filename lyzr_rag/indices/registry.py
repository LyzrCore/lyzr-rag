"""Index registry."""

from typing import Dict, Type

from lyzr_rag.data_structs.struct_type import IndexStructType
from lyzr_rag.indices.base import BaseIndex
from lyzr_rag.indices.document_summary.base import DocumentSummaryIndex
from lyzr_rag.indices.empty.base import EmptyIndex
from lyzr_rag.indices.keyword_table.base import KeywordTableIndex
from lyzr_rag.indices.knowledge_graph.base import KnowledgeGraphIndex
from lyzr_rag.indices.list.base import SummaryIndex
from lyzr_rag.indices.multi_modal import MultiModalVectorStoreIndex
from lyzr_rag.indices.struct_store.pandas import PandasIndex
from lyzr_rag.indices.struct_store.sql import SQLStructStoreIndex
from lyzr_rag.indices.tree.base import TreeIndex
from lyzr_rag.indices.vector_store.base import VectorStoreIndex

INDEX_STRUCT_TYPE_TO_INDEX_CLASS: Dict[IndexStructType, Type[BaseIndex]] = {
    IndexStructType.TREE: TreeIndex,
    IndexStructType.LIST: SummaryIndex,
    IndexStructType.KEYWORD_TABLE: KeywordTableIndex,
    IndexStructType.VECTOR_STORE: VectorStoreIndex,
    IndexStructType.SQL: SQLStructStoreIndex,
    IndexStructType.PANDAS: PandasIndex,
    IndexStructType.KG: KnowledgeGraphIndex,
    IndexStructType.EMPTY: EmptyIndex,
    IndexStructType.DOCUMENT_SUMMARY: DocumentSummaryIndex,
    IndexStructType.MULTIMODAL_VECTOR_STORE: MultiModalVectorStoreIndex,
}
