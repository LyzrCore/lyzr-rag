from typing import Dict, Type

from lyzr_rag.llms.bedrock import Bedrock
from lyzr_rag.llms.custom import CustomLLM
from lyzr_rag.llms.gradient import GradientBaseModelLLM, GradientModelAdapterLLM
from lyzr_rag.llms.huggingface import HuggingFaceLLM
from lyzr_rag.llms.langchain import LangChainLLM
from lyzr_rag.llms.llama_cpp import LlamaCPP
from lyzr_rag.llms.llm import LLM
from lyzr_rag.llms.mock import MockLLM
from lyzr_rag.llms.openai import OpenAI
from lyzr_rag.llms.palm import PaLM
from lyzr_rag.llms.predibase import PredibaseLLM
from lyzr_rag.llms.replicate import Replicate
from lyzr_rag.llms.vertex import Vertex
from lyzr_rag.llms.xinference import Xinference

RECOGNIZED_LLMS: Dict[str, Type[LLM]] = {
    MockLLM.class_name(): MockLLM,
    Replicate.class_name(): Replicate,
    HuggingFaceLLM.class_name(): HuggingFaceLLM,
    OpenAI.class_name(): OpenAI,
    Xinference.class_name(): Xinference,
    LlamaCPP.class_name(): LlamaCPP,
    LangChainLLM.class_name(): LangChainLLM,
    PaLM.class_name(): PaLM,
    PredibaseLLM.class_name(): PredibaseLLM,
    Bedrock.class_name(): Bedrock,
    CustomLLM.class_name(): CustomLLM,
    GradientBaseModelLLM.class_name(): GradientBaseModelLLM,
    GradientModelAdapterLLM.class_name(): GradientModelAdapterLLM,
    Vertex.class_name(): Vertex,
}


def load_llm(data: dict) -> LLM:
    """Load LLM by name."""
    if isinstance(data, LLM):
        return data
    llm_name = data.get("class_name", None)
    if llm_name is None:
        raise ValueError("LLM loading requires a class_name")

    if llm_name not in RECOGNIZED_LLMS:
        raise ValueError(f"Invalid LLM name: {llm_name}")

    return RECOGNIZED_LLMS[llm_name].from_dict(data)
