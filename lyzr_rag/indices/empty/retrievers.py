"""Default query for EmptyIndex."""
from typing import Any, List, Optional

from lyzr_rag.callbacks.base import CallbackManager
from lyzr_rag.core.base_retriever import BaseRetriever
from lyzr_rag.indices.empty.base import EmptyIndex
from lyzr_rag.prompts import BasePromptTemplate
from lyzr_rag.prompts.default_prompts import DEFAULT_SIMPLE_INPUT_PROMPT
from lyzr_rag.schema import NodeWithScore, QueryBundle


class EmptyIndexRetriever(BaseRetriever):
    """EmptyIndex query.

    Passes the raw LLM call to the underlying LLM model.

    Args:
        input_prompt (Optional[BasePromptTemplate]): A Simple Input Prompt
            (see :ref:`Prompt-Templates`).

    """

    def __init__(
        self,
        index: EmptyIndex,
        input_prompt: Optional[BasePromptTemplate] = None,
        callback_manager: Optional[CallbackManager] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize params."""
        self._index = index
        self._input_prompt = input_prompt or DEFAULT_SIMPLE_INPUT_PROMPT
        super().__init__(callback_manager)

    def _retrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
        """Retrieve relevant nodes."""
        del query_bundle  # Unused
        return []
