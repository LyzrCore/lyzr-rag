"""Embedding utils for LlamaIndex."""

import os
from typing import TYPE_CHECKING, List, Optional, Union

if TYPE_CHECKING:
    from lyzr_rag.bridge.langchain import Embeddings as LCEmbeddings
from lyzr_rag.embeddings.base import BaseEmbedding
from lyzr_rag.embeddings.clip import ClipEmbedding
from lyzr_rag.embeddings.huggingface import HuggingFaceEmbedding
from lyzr_rag.embeddings.huggingface_utils import (
    INSTRUCTOR_MODELS,
)
from lyzr_rag.embeddings.instructor import InstructorEmbedding
from lyzr_rag.embeddings.langchain import LangchainEmbedding
from lyzr_rag.embeddings.openai import OpenAIEmbedding
from lyzr_rag.llms.openai_utils import validate_openai_api_key
from lyzr_rag.token_counter.mock_embed_model import MockEmbedding
from lyzr_rag.utils import get_cache_dir

EmbedType = Union[BaseEmbedding, "LCEmbeddings", str]


def save_embedding(embedding: List[float], file_path: str) -> None:
    """Save embedding to file."""
    with open(file_path, "w") as f:
        f.write(",".join([str(x) for x in embedding]))


def load_embedding(file_path: str) -> List[float]:
    """Load embedding from file. Will only return first embedding in file."""
    with open(file_path) as f:
        for line in f:
            embedding = [float(x) for x in line.strip().split(",")]
            break
        return embedding


def resolve_embed_model(embed_model: Optional[EmbedType] = None) -> BaseEmbedding:
    """Resolve embed model."""
    try:
        from lyzr_rag.bridge.langchain import Embeddings as LCEmbeddings
    except ImportError:
        LCEmbeddings = None  # type: ignore

    if embed_model == "default":
        try:
            embed_model = OpenAIEmbedding()
            validate_openai_api_key(embed_model.api_key)
        except ValueError as e:
            raise ValueError(
                "\n******\n"
                "Could not load OpenAI embedding model. "
                "If you intended to use OpenAI, please check your OPENAI_API_KEY.\n"
                "Original error:\n"
                f"{e!s}"
                "\nConsider using embed_model='local'.\n"
                "Visit our documentation for more embedding options: "
                "https://docs.lyzr.ai/"
                "embeddings.html#modules"
                "\n******"
            )

    # for image embeddings
    if embed_model == "clip":
        embed_model = ClipEmbedding()

    if isinstance(embed_model, str):
        splits = embed_model.split(":", 1)
        is_local = splits[0]
        model_name = splits[1] if len(splits) > 1 else None
        if is_local != "local":
            raise ValueError(
                "embed_model must start with str 'local' or of type BaseEmbedding"
            )

        cache_folder = os.path.join(get_cache_dir(), "models")
        os.makedirs(cache_folder, exist_ok=True)

        if model_name in INSTRUCTOR_MODELS:
            embed_model = InstructorEmbedding(
                model_name=model_name, cache_folder=cache_folder
            )
        else:
            embed_model = HuggingFaceEmbedding(
                model_name=model_name, cache_folder=cache_folder
            )

    if LCEmbeddings is not None and isinstance(embed_model, LCEmbeddings):
        embed_model = LangchainEmbedding(embed_model)

    if embed_model is None:
        print("Embeddings have been explicitly disabled. Using MockEmbedding.")
        embed_model = MockEmbedding(embed_dim=1)

    return embed_model
