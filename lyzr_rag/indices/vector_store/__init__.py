"""Vector-store based data structures."""

from lyzr_rag.indices.vector_store.base import GPTVectorStoreIndex, VectorStoreIndex
from lyzr_rag.indices.vector_store.retrievers import (
    VectorIndexAutoRetriever,
    VectorIndexRetriever,
)

__all__ = [
    "VectorStoreIndex",
    "VectorIndexRetriever",
    "VectorIndexAutoRetriever",
    # legacy
    "GPTVectorStoreIndex",
]
