"""Agent utils."""

from lyzr_rag.agent.types import TaskStep
from lyzr_rag.core.llms.types import MessageRole
from lyzr_rag.llms.base import ChatMessage
from lyzr_rag.memory import BaseMemory


def add_user_step_to_memory(
    step: TaskStep, memory: BaseMemory, verbose: bool = False
) -> None:
    """Add user step to memory."""
    user_message = ChatMessage(content=step.input, role=MessageRole.USER)
    memory.put(user_message)
    if verbose:
        print(f"Added user message to memory: {step.input}")
