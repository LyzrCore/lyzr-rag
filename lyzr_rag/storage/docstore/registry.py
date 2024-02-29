from enum import Enum
from typing import Dict, Type

from lyzr_rag.storage.docstore.mongo_docstore import MongoDocumentStore
from lyzr_rag.storage.docstore.simple_docstore import SimpleDocumentStore
from lyzr_rag.storage.docstore.types import BaseDocumentStore


class DocumentStoreType(str, Enum):
    MONGO = "mongo"
    SIMPLE = "simple"


DOCSTORE_TYPE_TO_CLASS: Dict[DocumentStoreType, Type[BaseDocumentStore]] = {
    DocumentStoreType.MONGO: MongoDocumentStore,
    DocumentStoreType.SIMPLE: SimpleDocumentStore,
}


DOCSTORE_CLASS_TO_TYPE: Dict[Type[BaseDocumentStore], DocumentStoreType] = {
    cls_: type_ for type_, cls_ in DOCSTORE_TYPE_TO_CLASS.items()
}


def get_default_docstore() -> BaseDocumentStore:
    return SimpleDocumentStore()
