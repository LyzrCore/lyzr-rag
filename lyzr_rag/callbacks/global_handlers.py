"""Global eval handlers."""

from typing import Any

from lyzr_rag.callbacks.argilla_callback import argilla_callback_handler
from lyzr_rag.callbacks.arize_phoenix_callback import arize_phoenix_callback_handler
from lyzr_rag.callbacks.base_handler import BaseCallbackHandler
from lyzr_rag.callbacks.deepeval_callback import deepeval_callback_handler
from lyzr_rag.callbacks.honeyhive_callback import honeyhive_callback_handler
from lyzr_rag.callbacks.open_inference_callback import OpenInferenceCallbackHandler
from lyzr_rag.callbacks.promptlayer_handler import PromptLayerHandler
from lyzr_rag.callbacks.simple_llm_handler import SimpleLLMHandler
from lyzr_rag.callbacks.wandb_callback import WandbCallbackHandler


def set_global_handler(eval_mode: str, **eval_params: Any) -> None:
    """Set global eval handlers."""
    import lyzr_rag

    lyzr_rag.global_handler = create_global_handler(eval_mode, **eval_params)


def create_global_handler(eval_mode: str, **eval_params: Any) -> BaseCallbackHandler:
    """Get global eval handler."""
    if eval_mode == "wandb":
        handler: BaseCallbackHandler = WandbCallbackHandler(**eval_params)
    elif eval_mode == "openinference":
        handler = OpenInferenceCallbackHandler(**eval_params)
    elif eval_mode == "arize_phoenix":
        handler = arize_phoenix_callback_handler(**eval_params)
    elif eval_mode == "honeyhive":
        handler = honeyhive_callback_handler(**eval_params)
    elif eval_mode == "promptlayer":
        handler = PromptLayerHandler(**eval_params)
    elif eval_mode == "deepeval":
        handler = deepeval_callback_handler(**eval_params)
    elif eval_mode == "simple":
        handler = SimpleLLMHandler(**eval_params)
    elif eval_mode == "argilla":
        handler = argilla_callback_handler(**eval_params)
    else:
        raise ValueError(f"Eval mode {eval_mode} not supported.")

    return handler
