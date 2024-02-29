"""Init file for langchain helpers."""

try:
    import langchain  # noqa
except ImportError:
    raise ImportError(
        "langchain not installed. "
        "Please install langchain with `pip install lyzr_rag[langchain]`."
    )
