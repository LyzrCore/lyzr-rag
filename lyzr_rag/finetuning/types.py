"""Finetuning Engine."""

from abc import ABC, abstractmethod
from typing import Any

from lyzr_rag.embeddings.base import BaseEmbedding
from lyzr_rag.llms.llm import LLM
from lyzr_rag.postprocessor import CohereRerank, SentenceTransformerRerank


class BaseLLMFinetuneEngine(ABC):
    """Base LLM finetuning engine."""

    @abstractmethod
    def finetune(self) -> None:
        """Goes off and does stuff."""

    @abstractmethod
    def get_finetuned_model(self, **model_kwargs: Any) -> LLM:
        """Gets finetuned model."""


class BaseEmbeddingFinetuneEngine(ABC):
    """Base Embedding finetuning engine."""

    @abstractmethod
    def finetune(self) -> None:
        """Goes off and does stuff."""

    @abstractmethod
    def get_finetuned_model(self, **model_kwargs: Any) -> BaseEmbedding:
        """Gets finetuned model."""


class BaseCrossEncoderFinetuningEngine(ABC):
    """Base Cross Encoder Finetuning Engine."""

    @abstractmethod
    def finetune(self) -> None:
        """Goes off and does stuff."""

    @abstractmethod
    def get_finetuned_model(
        self, model_name: str, top_n: int = 3
    ) -> SentenceTransformerRerank:
        """Gets fine-tuned Cross-Encoder model as re-ranker."""


class BaseCohereRerankerFinetuningEngine(ABC):
    """Base Cohere Reranker Finetuning Engine."""

    @abstractmethod
    def finetune(self) -> None:
        """Goes off and does stuff."""

    @abstractmethod
    def get_finetuned_model(self, top_n: int = 5) -> CohereRerank:
        """Gets finetuned model."""
