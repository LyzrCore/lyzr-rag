from enum import Enum
from typing import Dict, Type

from lyzr_rag.vector_stores.bagel import BagelVectorStore
from lyzr_rag.vector_stores.cassandra import CassandraVectorStore
from lyzr_rag.vector_stores.chatgpt_plugin import ChatGPTRetrievalPluginClient
from lyzr_rag.vector_stores.chroma import ChromaVectorStore
from lyzr_rag.vector_stores.deeplake import DeepLakeVectorStore
from lyzr_rag.vector_stores.epsilla import EpsillaVectorStore
from lyzr_rag.vector_stores.faiss import FaissVectorStore
from lyzr_rag.vector_stores.jaguar import JaguarVectorStore
from lyzr_rag.vector_stores.lancedb import LanceDBVectorStore
from lyzr_rag.vector_stores.milvus import MilvusVectorStore
from lyzr_rag.vector_stores.myscale import MyScaleVectorStore
from lyzr_rag.vector_stores.opensearch import OpensearchVectorStore
from lyzr_rag.vector_stores.pinecone import PineconeVectorStore
from lyzr_rag.vector_stores.qdrant import QdrantVectorStore
from lyzr_rag.vector_stores.redis import RedisVectorStore
from lyzr_rag.vector_stores.rocksetdb import RocksetVectorStore
from lyzr_rag.vector_stores.simple import SimpleVectorStore
from lyzr_rag.vector_stores.supabase import SupabaseVectorStore
from lyzr_rag.vector_stores.txtai import TxtaiVectorStore
from lyzr_rag.vector_stores.types import VectorStore
from lyzr_rag.vector_stores.upstash import UpstashVectorStore
from lyzr_rag.vector_stores.weaviate import WeaviateVectorStore


class VectorStoreType(str, Enum):
    SIMPLE = "simple"
    REDIS = "redis"
    WEAVIATE = "weaviate"
    QDRANT = "qdrant"
    PINECONE = "pinecone"
    OPENSEARCH = "opensearch"
    FAISS = "faiss"
    TXTAI = "txtai"
    CASSANDRA = "cassandra"
    CHROMA = "chroma"
    CHATGPT_PLUGIN = "chatgpt_plugin"
    LANCEDB = "lancedb"
    MILVUS = "milvus"
    DEEPLAKE = "deeplake"
    MYSCALE = "myscale"
    SUPABASE = "supabase"
    ROCKSET = "rockset"
    BAGEL = "bagel"
    EPSILLA = "epsilla"
    JAGUAR = "jaguar"
    UPSTASH = "upstash"


VECTOR_STORE_TYPE_TO_VECTOR_STORE_CLASS: Dict[VectorStoreType, Type[VectorStore]] = {
    VectorStoreType.SIMPLE: SimpleVectorStore,
    VectorStoreType.REDIS: RedisVectorStore,
    VectorStoreType.WEAVIATE: WeaviateVectorStore,
    VectorStoreType.QDRANT: QdrantVectorStore,
    VectorStoreType.LANCEDB: LanceDBVectorStore,
    VectorStoreType.SUPABASE: SupabaseVectorStore,
    VectorStoreType.MILVUS: MilvusVectorStore,
    VectorStoreType.PINECONE: PineconeVectorStore,
    VectorStoreType.OPENSEARCH: OpensearchVectorStore,
    VectorStoreType.FAISS: FaissVectorStore,
    VectorStoreType.TXTAI: TxtaiVectorStore,
    VectorStoreType.CASSANDRA: CassandraVectorStore,
    VectorStoreType.CHROMA: ChromaVectorStore,
    VectorStoreType.CHATGPT_PLUGIN: ChatGPTRetrievalPluginClient,
    VectorStoreType.DEEPLAKE: DeepLakeVectorStore,
    VectorStoreType.MYSCALE: MyScaleVectorStore,
    VectorStoreType.ROCKSET: RocksetVectorStore,
    VectorStoreType.BAGEL: BagelVectorStore,
    VectorStoreType.EPSILLA: EpsillaVectorStore,
    VectorStoreType.JAGUAR: JaguarVectorStore,
    VectorStoreType.UPSTASH: UpstashVectorStore,
}

VECTOR_STORE_CLASS_TO_VECTOR_STORE_TYPE: Dict[Type[VectorStore], VectorStoreType] = {
    cls_: type_ for type_, cls_ in VECTOR_STORE_TYPE_TO_VECTOR_STORE_CLASS.items()
}
