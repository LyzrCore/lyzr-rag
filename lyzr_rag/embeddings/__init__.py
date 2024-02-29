"""Init file."""

from lyzr_rag.embeddings.adapter import (
    AdapterEmbeddingModel,
    LinearAdapterEmbeddingModel,
)
from lyzr_rag.embeddings.anyscale import AnyscaleEmbedding
from lyzr_rag.embeddings.azure_openai import AzureOpenAIEmbedding
from lyzr_rag.embeddings.base import BaseEmbedding, SimilarityMode
from lyzr_rag.embeddings.bedrock import BedrockEmbedding
from lyzr_rag.embeddings.clarifai import ClarifaiEmbedding
from lyzr_rag.embeddings.clip import ClipEmbedding
from lyzr_rag.embeddings.cohereai import CohereEmbedding
from lyzr_rag.embeddings.dashscope import (
    DashScopeBatchTextEmbeddingModels,
    DashScopeEmbedding,
    DashScopeMultiModalEmbeddingModels,
    DashScopeTextEmbeddingModels,
    DashScopeTextEmbeddingType,
)
from lyzr_rag.embeddings.elasticsearch import (
    ElasticsearchEmbedding,
    ElasticsearchEmbeddings,
)
from lyzr_rag.embeddings.fastembed import FastEmbedEmbedding
from lyzr_rag.embeddings.gemini import GeminiEmbedding
from lyzr_rag.embeddings.google import GoogleUnivSentEncoderEmbedding
from lyzr_rag.embeddings.google_palm import GooglePaLMEmbedding
from lyzr_rag.embeddings.gradient import GradientEmbedding
from lyzr_rag.embeddings.huggingface import (
    HuggingFaceEmbedding,
    HuggingFaceInferenceAPIEmbedding,
    HuggingFaceInferenceAPIEmbeddings,
)
from lyzr_rag.embeddings.huggingface_optimum import OptimumEmbedding
from lyzr_rag.embeddings.huggingface_utils import DEFAULT_HUGGINGFACE_EMBEDDING_MODEL
from lyzr_rag.embeddings.instructor import InstructorEmbedding
from lyzr_rag.embeddings.langchain import LangchainEmbedding
from lyzr_rag.embeddings.llm_rails import LLMRailsEmbedding, LLMRailsEmbeddings
from lyzr_rag.embeddings.mistralai import MistralAIEmbedding
from lyzr_rag.embeddings.nomic import NomicEmbedding
from lyzr_rag.embeddings.ollama_embedding import OllamaEmbedding
from lyzr_rag.embeddings.openai import OpenAIEmbedding
from lyzr_rag.embeddings.pooling import Pooling
from lyzr_rag.embeddings.sagemaker_embedding_endpoint import (
    SageMakerEmbedding,
)
from lyzr_rag.embeddings.text_embeddings_inference import TextEmbeddingsInference
from lyzr_rag.embeddings.together import TogetherEmbedding
from lyzr_rag.embeddings.utils import resolve_embed_model
from lyzr_rag.embeddings.voyageai import VoyageEmbedding

__all__ = [
    "AdapterEmbeddingModel",
    "BedrockEmbedding",
    "ClarifaiEmbedding",
    "ClipEmbedding",
    "CohereEmbedding",
    "BaseEmbedding",
    "DEFAULT_HUGGINGFACE_EMBEDDING_MODEL",
    "ElasticsearchEmbedding",
    "FastEmbedEmbedding",
    "GoogleUnivSentEncoderEmbedding",
    "GradientEmbedding",
    "HuggingFaceInferenceAPIEmbedding",
    "HuggingFaceEmbedding",
    "InstructorEmbedding",
    "LangchainEmbedding",
    "LinearAdapterEmbeddingModel",
    "LLMRailsEmbedding",
    "MistralAIEmbedding",
    "OpenAIEmbedding",
    "AzureOpenAIEmbedding",
    "AnyscaleEmbedding",
    "OptimumEmbedding",
    "Pooling",
    "SageMakerEmbedding",
    "GooglePaLMEmbedding",
    "SimilarityMode",
    "TextEmbeddingsInference",
    "TogetherEmbedding",
    "resolve_embed_model",
    "NomicEmbedding",
    # Deprecated, kept for backwards compatibility
    "LLMRailsEmbeddings",
    "ElasticsearchEmbeddings",
    "HuggingFaceInferenceAPIEmbeddings",
    "VoyageEmbedding",
    "OllamaEmbedding",
    "GeminiEmbedding",
    "DashScopeEmbedding",
    "DashScopeTextEmbeddingModels",
    "DashScopeTextEmbeddingType",
    "DashScopeBatchTextEmbeddingModels",
    "DashScopeMultiModalEmbeddingModels",
]
