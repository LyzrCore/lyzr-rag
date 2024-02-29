from typing import Any

from lyzr_rag.callbacks.base_handler import BaseCallbackHandler


def argilla_callback_handler(**kwargs: Any) -> BaseCallbackHandler:
    try:
        # lazy import
        from argilla_lyzr_rag import ArgillaCallbackHandler
    except ImportError:
        raise ImportError("Please install Argilla with `pip install argilla`")
    return ArgillaCallbackHandler(**kwargs)
