from abc import abstractmethod
from typing import List, Sequence

from lyzr_rag.bridge.pydantic import BaseModel
from lyzr_rag.prompts.mixin import PromptMixin, PromptMixinType
from lyzr_rag.schema import QueryBundle
from lyzr_rag.tools.types import ToolMetadata


class SubQuestion(BaseModel):
    sub_question: str
    tool_name: str


class SubQuestionList(BaseModel):
    """A pydantic object wrapping a list of sub-questions.

    This is mostly used to make getting a json schema easier.
    """

    items: List[SubQuestion]


class BaseQuestionGenerator(PromptMixin):
    def _get_prompt_modules(self) -> PromptMixinType:
        """Get prompt modules."""
        return {}

    @abstractmethod
    def generate(
        self, tools: Sequence[ToolMetadata], query: QueryBundle
    ) -> List[SubQuestion]:
        pass

    @abstractmethod
    async def agenerate(
        self, tools: Sequence[ToolMetadata], query: QueryBundle
    ) -> List[SubQuestion]:
        pass
