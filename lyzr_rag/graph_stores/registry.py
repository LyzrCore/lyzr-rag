from enum import Enum
from typing import Dict, Type

from lyzr_rag.graph_stores.falkordb import FalkorDBGraphStore
from lyzr_rag.graph_stores.kuzu import KuzuGraphStore
from lyzr_rag.graph_stores.nebulagraph import NebulaGraphStore
from lyzr_rag.graph_stores.neo4j import Neo4jGraphStore
from lyzr_rag.graph_stores.simple import SimpleGraphStore
from lyzr_rag.graph_stores.types import GraphStore


class GraphStoreType(str, Enum):
    SIMPLE = "simple_kg"
    NEBULA = "nebulagraph"
    KUZU = "kuzu"
    NEO4J = "neo4j"
    FALKORDB = "falkordb"


GRAPH_STORE_TYPE_TO_GRAPH_STORE_CLASS: Dict[GraphStoreType, Type[GraphStore]] = {
    GraphStoreType.SIMPLE: SimpleGraphStore,
    GraphStoreType.NEBULA: NebulaGraphStore,
    GraphStoreType.KUZU: KuzuGraphStore,
    GraphStoreType.NEO4J: Neo4jGraphStore,
    GraphStoreType.FALKORDB: FalkorDBGraphStore,
}

GRAPH_STORE_CLASS_TO_GRAPH_STORE_TYPE: Dict[Type[GraphStore], GraphStoreType] = {
    cls_: type_ for type_, cls_ in GRAPH_STORE_TYPE_TO_GRAPH_STORE_CLASS.items()
}
