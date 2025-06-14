"""
Rule-based markdown evaluator implementation.
"""

import logging
from pathlib import Path
from typing import Optional

from co_op_translator.core.llm.markdown_evaluator import MarkdownEvaluator

logger = logging.getLogger(__name__)


class RuleBasedMarkdownEvaluator(MarkdownEvaluator):
    """
    A concrete implementation of MarkdownEvaluator that only uses rule-based evaluation.

    This implementation provides a dummy implementation of the _run_prompt method
    since it doesn't actually use LLM for evaluation.
    """

    def __init__(
        self,
        root_dir: Optional[Path] = None,
        use_rule: bool = True,
    ):
        """
        Initialize the rule-based markdown evaluator.

        Args:
            root_dir: Root directory of the project for path calculations
            use_rule: Whether to use rule-based evaluation
        """
        super().__init__(root_dir=root_dir, use_llm=False, use_rule=use_rule)

    async def _run_prompt(self, prompt: str, index: int, total: int) -> str:
        """
        Dummy implementation of _run_prompt for the rule-based evaluator.

        Since this evaluator doesn't use LLM, this method should never be called.
        If it is called, it logs a warning and returns an empty string.

        Args:
            prompt: The evaluation prompt that would be sent to an LLM
            index: Current chunk index for progress tracking
            total: Total number of chunks for progress reporting

        Returns:
            Empty string as this evaluator doesn't use LLM
        """
        logger.warning(
            "RuleBasedMarkdownEvaluator._run_prompt was called, but this "
            "evaluator doesn't support LLM-based evaluation."
        )
        return ""
