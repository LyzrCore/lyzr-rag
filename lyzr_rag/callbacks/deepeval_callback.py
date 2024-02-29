from typing import Any

from lyzr_rag.callbacks.base_handler import BaseCallbackHandler


def deepeval_callback_handler(**kwargs: Any) -> BaseCallbackHandler:
    try:
        from deepeval.tracing.integrations.lyzr_rag import LlamaIndexCallbackHandler
    except ImportError:
        raise ImportError("Please install DeepEval with `pip install -U deepeval`")
    return LlamaIndexCallbackHandler(**kwargs)
