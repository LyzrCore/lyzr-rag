from typing import List, Optional, Sequence, cast

from lyzr_rag.llm_predictor.base import LLMPredictorType
from lyzr_rag.output_parsers.base import StructuredOutput
from lyzr_rag.prompts.base import BasePromptTemplate, PromptTemplate
from lyzr_rag.prompts.mixin import PromptDictType
from lyzr_rag.prompts.prompt_type import PromptType
from lyzr_rag.question_gen.output_parser import SubQuestionOutputParser
from lyzr_rag.question_gen.prompts import (
    DEFAULT_SUB_QUESTION_PROMPT_TMPL,
    build_tools_text,
)
from lyzr_rag.question_gen.types import BaseQuestionGenerator, SubQuestion
from lyzr_rag.schema import QueryBundle
from lyzr_rag.service_context import ServiceContext
from lyzr_rag.tools.types import ToolMetadata
from lyzr_rag.types import BaseOutputParser


class LLMQuestionGenerator(BaseQuestionGenerator):
    def __init__(
        self,
        llm: LLMPredictorType,
        prompt: BasePromptTemplate,
    ) -> None:
        self._llm = llm
        self._prompt = prompt

        if self._prompt.output_parser is None:
            raise ValueError("Prompt should have output parser.")

    @classmethod
    def from_defaults(
        cls,
        service_context: Optional[ServiceContext] = None,
        prompt_template_str: Optional[str] = None,
        output_parser: Optional[BaseOutputParser] = None,
    ) -> "LLMQuestionGenerator":
        # optionally initialize defaults
        service_context = service_context or ServiceContext.from_defaults()
        prompt_template_str = prompt_template_str or DEFAULT_SUB_QUESTION_PROMPT_TMPL
        output_parser = output_parser or SubQuestionOutputParser()

        # construct prompt
        prompt = PromptTemplate(
            template=prompt_template_str,
            output_parser=output_parser,
            prompt_type=PromptType.SUB_QUESTION,
        )
        return cls(service_context.llm, prompt)

    def _get_prompts(self) -> PromptDictType:
        """Get prompts."""
        return {"question_gen_prompt": self._prompt}

    def _update_prompts(self, prompts: PromptDictType) -> None:
        """Update prompts."""
        if "question_gen_prompt" in prompts:
            output_parser = prompts["question_gen_prompt"].output_parser
            if output_parser is None:
                output_parser = SubQuestionOutputParser()
            self._prompt = PromptTemplate(
                prompts["question_gen_prompt"].template, output_parser=output_parser
            )

    def generate(
        self, tools: Sequence[ToolMetadata], query: QueryBundle
    ) -> List[SubQuestion]:
        tools_str = build_tools_text(tools)
        query_str = query.query_str
        prediction = self._llm.predict(
            prompt=self._prompt,
            tools_str=tools_str,
            query_str=query_str,
        )

        assert self._prompt.output_parser is not None
        parse = self._prompt.output_parser.parse(prediction)
        parse = cast(StructuredOutput, parse)
        return parse.parsed_output

    async def agenerate(
        self, tools: Sequence[ToolMetadata], query: QueryBundle
    ) -> List[SubQuestion]:
        tools_str = build_tools_text(tools)
        query_str = query.query_str
        prediction = await self._llm.apredict(
            prompt=self._prompt,
            tools_str=tools_str,
            query_str=query_str,
        )

        assert self._prompt.output_parser is not None
        parse = self._prompt.output_parser.parse(prediction)
        parse = cast(StructuredOutput, parse)
        return parse.parsed_output
