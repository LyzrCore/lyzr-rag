from typing import Any, Sequence

from lyzr_rag.prompts.mixin import PromptDictType
from lyzr_rag.response_synthesizers.base import BaseSynthesizer
from lyzr_rag.types import RESPONSE_TEXT_TYPE


class NoText(BaseSynthesizer):
    def _get_prompts(self) -> PromptDictType:
        """Get prompts."""
        return {}

    def _update_prompts(self, prompts: PromptDictType) -> None:
        """Update prompts."""

    def get_response(
        self,
        query_str: str,
        text_chunks: Sequence[str],
        **response_kwargs: Any,
    ) -> RESPONSE_TEXT_TYPE:
        return ""

    async def aget_response(
        self,
        query_str: str,
        text_chunks: Sequence[str],
        **response_kwargs: Any,
    ) -> RESPONSE_TEXT_TYPE:
        return ""
