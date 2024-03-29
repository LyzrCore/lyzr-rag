"""base multi modal retriever."""

from abc import abstractmethod
from typing import List

from lyzr_rag.core.base_retriever import BaseRetriever
from lyzr_rag.core.image_retriever import BaseImageRetriever
from lyzr_rag.indices.query.schema import QueryType
from lyzr_rag.schema import NodeWithScore


class MultiModalRetriever(BaseRetriever, BaseImageRetriever):
    """Multi Modal base retriever."""

    @abstractmethod
    def text_retrieve(self, str_or_query_bundle: QueryType) -> List[NodeWithScore]:
        """Retrieve text nodes given text query.

        Implemented by the user.

        """

    @abstractmethod
    def text_to_image_retrieve(
        self, str_or_query_bundle: QueryType
    ) -> List[NodeWithScore]:
        """Retrieve image nodes given text query.

        Implemented by the user.

        """

    @abstractmethod
    def image_to_image_retrieve(
        self, str_or_query_bundle: QueryType
    ) -> List[NodeWithScore]:
        """Retrieve image nodes given image query.

        Implemented by the user.

        """

    @abstractmethod
    async def atext_retrieve(
        self, str_or_query_bundle: QueryType
    ) -> List[NodeWithScore]:
        """Async Retrieve text nodes given text query.

        Implemented by the user.

        """

    @abstractmethod
    async def atext_to_image_retrieve(
        self, str_or_query_bundle: QueryType
    ) -> List[NodeWithScore]:
        """Async Retrieve image nodes given text query.

        Implemented by the user.

        """

    @abstractmethod
    async def aimage_to_image_retrieve(
        self, str_or_query_bundle: QueryType
    ) -> List[NodeWithScore]:
        """Async Retrieve image nodes given image query.

        Implemented by the user.

        """
