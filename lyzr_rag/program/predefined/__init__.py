"""Init params."""

from lyzr_rag.program.predefined.evaporate.base import (
    DFEvaporateProgram,
    MultiValueEvaporateProgram,
)
from lyzr_rag.program.predefined.evaporate.extractor import EvaporateExtractor

__all__ = [
    "EvaporateExtractor",
    "DFEvaporateProgram",
    "MultiValueEvaporateProgram",
]
