"""Evaluation modules."""

from lyzr_rag.evaluation.answer_relevancy import AnswerRelevancyEvaluator
from lyzr_rag.evaluation.base import (
    BaseEvaluator,
    EvaluationResult,
)
from lyzr_rag.evaluation.batch_runner import BatchEvalRunner
from lyzr_rag.evaluation.context_relevancy import ContextRelevancyEvaluator
from lyzr_rag.evaluation.correctness import CorrectnessEvaluator
from lyzr_rag.evaluation.dataset_generation import (
    DatasetGenerator,
    QueryResponseDataset,
)
from lyzr_rag.evaluation.faithfulness import FaithfulnessEvaluator, ResponseEvaluator
from lyzr_rag.evaluation.guideline import GuidelineEvaluator
from lyzr_rag.evaluation.notebook_utils import get_retrieval_results_df
from lyzr_rag.evaluation.pairwise import PairwiseComparisonEvaluator
from lyzr_rag.evaluation.relevancy import QueryResponseEvaluator, RelevancyEvaluator
from lyzr_rag.evaluation.retrieval.base import (
    BaseRetrievalEvaluator,
    RetrievalEvalResult,
)
from lyzr_rag.evaluation.retrieval.evaluator import (
    MultiModalRetrieverEvaluator,
    RetrieverEvaluator,
)
from lyzr_rag.evaluation.retrieval.metrics import (
    MRR,
    HitRate,
    RetrievalMetricResult,
    resolve_metrics,
)
from lyzr_rag.evaluation.semantic_similarity import SemanticSimilarityEvaluator
from lyzr_rag.evaluation.tonic_validate.answer_consistency import (
    AnswerConsistencyEvaluator,
)
from lyzr_rag.evaluation.tonic_validate.answer_consistency_binary import (
    AnswerConsistencyBinaryEvaluator,
)
from lyzr_rag.evaluation.tonic_validate.answer_similarity import (
    AnswerSimilarityEvaluator,
)
from lyzr_rag.evaluation.tonic_validate.augmentation_accuracy import (
    AugmentationAccuracyEvaluator,
)
from lyzr_rag.evaluation.tonic_validate.augmentation_precision import (
    AugmentationPrecisionEvaluator,
)
from lyzr_rag.evaluation.tonic_validate.retrieval_precision import (
    RetrievalPrecisionEvaluator,
)
from lyzr_rag.evaluation.tonic_validate.tonic_validate_evaluator import (
    TonicValidateEvaluator,
)

# import dataset generation too
from lyzr_rag.finetuning.embeddings.common import (
    EmbeddingQAFinetuneDataset,
    generate_qa_embedding_pairs,
)

# aliases for generate_qa_embedding_pairs
generate_question_context_pairs = generate_qa_embedding_pairs
LabelledQADataset = EmbeddingQAFinetuneDataset

__all__ = [
    "BaseEvaluator",
    "AnswerRelevancyEvaluator",
    "ContextRelevancyEvaluator",
    "EvaluationResult",
    "FaithfulnessEvaluator",
    "RelevancyEvaluator",
    "RelevanceEvaluator",
    "DatasetGenerator",
    "QueryResponseDataset",
    "GuidelineEvaluator",
    "CorrectnessEvaluator",
    "SemanticSimilarityEvaluator",
    "PairwiseComparisonEvaluator",
    "BatchEvalRunner",
    # legacy: kept for backward compatibility
    "QueryResponseEvaluator",
    "ResponseEvaluator",
    # retrieval
    "generate_qa_embedding_pairs",
    "generate_question_context_pairs",
    "EmbeddingQAFinetuneDataset",
    "BaseRetrievalEvaluator",
    "RetrievalEvalResult",
    "RetrieverEvaluator",
    "MultiModalRetrieverEvaluator",
    "RetrievalMetricResult",
    "resolve_metrics",
    "HitRate",
    "MRR",
    "get_retrieval_results_df",
    "LabelledQADataset",
    # tonic_validate evaluators
    "AnswerConsistencyEvaluator",
    "AnswerConsistencyBinaryEvaluator",
    "AnswerSimilarityEvaluator",
    "AugmentationAccuracyEvaluator",
    "AugmentationPrecisionEvaluator",
    "RetrievalPrecisionEvaluator",
    "TonicValidateEvaluator",
]
