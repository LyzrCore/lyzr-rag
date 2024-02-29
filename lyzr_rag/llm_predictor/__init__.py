"""Init params."""

from lyzr_rag.llm_predictor.base import LLMPredictor

# NOTE: this results in a circular import
# from lyzr_rag.llm_predictor.mock import MockLLMPredictor
from lyzr_rag.llm_predictor.structured import StructuredLLMPredictor

__all__ = [
    "LLMPredictor",
    # NOTE: this results in a circular import
    # "MockLLMPredictor",
    "StructuredLLMPredictor",
]
