from typing import Any

from lyzr_rag.output_parsers.base import StructuredOutput
from lyzr_rag.output_parsers.utils import parse_json_markdown
from lyzr_rag.types import BaseOutputParser
from lyzr_rag.vector_stores.types import VectorStoreQuerySpec


class VectorStoreQueryOutputParser(BaseOutputParser):
    def parse(self, output: str) -> Any:
        json_dict = parse_json_markdown(output)
        query_and_filters = VectorStoreQuerySpec.parse_obj(json_dict)

        return StructuredOutput(raw_output=output, parsed_output=query_and_filters)

    def format(self, prompt_template: str) -> str:
        return prompt_template
