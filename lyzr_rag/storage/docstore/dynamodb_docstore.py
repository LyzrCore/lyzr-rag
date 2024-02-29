from typing import Optional

from lyzr_rag.storage.docstore.keyval_docstore import KVDocumentStore
from lyzr_rag.storage.docstore.types import DEFAULT_BATCH_SIZE
from lyzr_rag.storage.kvstore.dynamodb_kvstore import DynamoDBKVStore


class DynamoDBDocumentStore(KVDocumentStore):
    def __init__(
        self,
        dynamodb_kvstore: DynamoDBKVStore,
        namespace: Optional[str] = None,
        batch_size: int = DEFAULT_BATCH_SIZE,
    ) -> None:
        super().__init__(
            kvstore=dynamodb_kvstore, namespace=namespace, batch_size=batch_size
        )

    @classmethod
    def from_table_name(
        cls, table_name: str, namespace: Optional[str] = None
    ) -> "DynamoDBDocumentStore":
        dynamodb_kvstore = DynamoDBKVStore.from_table_name(table_name=table_name)
        return cls(dynamodb_kvstore=dynamodb_kvstore, namespace=namespace)
