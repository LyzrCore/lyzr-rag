"""KG-based data structures."""

from lyzr_rag.indices.knowledge_graph.base import (
    GPTKnowledgeGraphIndex,
    KnowledgeGraphIndex,
)
from lyzr_rag.indices.knowledge_graph.retrievers import (
    KGTableRetriever,
    KnowledgeGraphRAGRetriever,
)

__all__ = [
    "KnowledgeGraphIndex",
    "KGTableRetriever",
    "KnowledgeGraphRAGRetriever",
    # legacy
    "GPTKnowledgeGraphIndex",
]
