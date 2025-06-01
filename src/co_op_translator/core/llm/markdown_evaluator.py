from abc import ABC, abstractmethod
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.utils.common.metadata_utils import (
    extract_metadata_from_content,
    format_metadata_comment,
)
from co_op_translator.utils.llm.markdown_utils import (
    generate_evaluation_prompt,
    process_markdown,
    replace_code_blocks_and_inline_code,
)

logger = logging.getLogger(__name__)


def evaluate_translation_rule_based(
    original_content: str, translated_content: str, language_code: str
) -> dict:
    """
    Perform rule-based evaluation of a translation.

    This function evaluates the translation quality based on simple rules like
    content length ratio, code block preservation, etc.

    Args:
        original_content: Content of the original file
        translated_content: Content of the translated file
        language_code: Language code of the translation

    Returns:
        dict: Evaluation results containing confidence score and any issues found
    """
    # Start with high confidence and decrease based on issues
    confidence_score = 1.0
    issues = []

    # Check if translation is significantly shorter or longer than original
    # This is a very simple heuristic that might need adjustment for different languages
    original_length = len(original_content)
    translated_length = len(translated_content)
    length_ratio = translated_length / original_length if original_length > 0 else 0

    # Different languages have different expected length ratios
    # For example, Asian languages might have shorter text than English
    expected_ratio_min = 0.5
    expected_ratio_max = 2.0

    if length_ratio < expected_ratio_min:
        confidence_score -= 0.3
        issues.append(f"Translation seems too short (ratio: {length_ratio:.2f})")
    elif length_ratio > expected_ratio_max:
        confidence_score -= 0.3
        issues.append(f"Translation seems too long (ratio: {length_ratio:.2f})")

    # Simple check for code blocks (very basic)
    orig_code_count = original_content.count("```")
    trans_code_count = translated_content.count("```")

    if orig_code_count != trans_code_count:
        confidence_score -= 0.2
        issues.append(
            f"Code block count mismatch: original={orig_code_count}, translation={trans_code_count}"
        )

    # Ensure confidence score stays within 0-1 range
    confidence_score = max(0.0, min(1.0, confidence_score))

    return {"confidence_score": confidence_score, "issues_found": issues}


class MarkdownEvaluator(ABC):
    """
    Class for evaluating the quality of markdown translations.

    This class provides methods to analyze translations, calculate confidence scores,
    and update metadata with evaluation results. It supports both rule-based evaluation
    and LLM-based evaluation when an LLM provider is configured.
    """

    def __init__(
        self,
        root_dir: Optional[Path] = None,
        use_llm: bool = True,
        use_rule: bool = True,
    ):
        """
        Initialize the markdown evaluator.

        Args:
            root_dir: Root directory of the project for path calculations
            use_llm: Whether to use LLM for enhanced evaluation (if available)
            use_rule: Whether to use rule-based evaluation
        """
        self.root_dir = root_dir
        self.use_llm = use_llm
        self.use_rule = use_rule

    @abstractmethod
    async def _run_prompt(self, prompt: str, index: int, total: int) -> str:
        """
        Execute a single evaluation prompt using the configured LLM provider.
        This is a base method that should be overridden by provider-specific subclasses.

        Args:
            prompt: The evaluation prompt to send to the LLM
            index: Current chunk index for progress tracking
            total: Total number of chunks for progress reporting

        Returns:
            The evaluation result as text

        Raises:
            NotImplementedError: If called directly on the base class
        """
        pass

    @classmethod
    def create(
        cls, root_dir: Path = None, use_llm: bool = True, use_rule: bool = True
    ) -> "MarkdownEvaluator":
        """Create appropriate markdown evaluator based on configured provider.

        Factory method that instantiates the correct implementation based on
        the LLM provider configuration.

        Args:
            root_dir: Root directory of the project for path calculations
            use_llm: Whether to use LLM for enhanced evaluation
            use_rule: Whether to use rule-based evaluation

        Returns:
            Appropriate evaluator implementation instance

        Raises:
            ValueError: If no valid LLM provider is configured
        """
        # If LLM is not requested, return base evaluator
        if not use_llm:
            return cls(root_dir=root_dir, use_llm=False, use_rule=use_rule)

        provider = LLMConfig.get_available_provider()
        if provider is None:
            raise ValueError("No valid LLM provider configured")

        if provider == LLMProvider.AZURE_OPENAI:
            from co_op_translator.core.llm.providers.azure.markdown_evaluator import (
                AzureMarkdownEvaluator,
            )

            return AzureMarkdownEvaluator(
                root_dir=root_dir, use_llm=use_llm, use_rule=use_rule
            )
        elif provider == LLMProvider.OPENAI:
            from co_op_translator.core.llm.providers.openai.markdown_evaluator import (
                OpenAIMarkdownEvaluator,
            )

            return OpenAIMarkdownEvaluator(
                root_dir=root_dir, use_llm=use_llm, use_rule=use_rule
            )
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    async def evaluate_markdown(
        self,
        original_file: Path,
        translated_file: Path,
        language_code: str,
        max_tokens: int = 2048,  # Using 2048 tokens for evaluation chunks
    ) -> Tuple[Dict, bool]:
        """
        Evaluate a translated markdown file against its original using chunk-based approach.

        Args:
            original_file: Path to the original markdown file
            translated_file: Path to the translated markdown file
            language_code: Target language code
            max_tokens: Maximum tokens per chunk for processing

        Returns:
            Tuple containing the evaluation results dictionary and a boolean indicating
            whether the metadata was successfully updated
        """
        try:
            # Read original and translated content
            with open(original_file, "r", encoding="utf-8") as f:
                original_content = f.read()

            with open(translated_file, "r", encoding="utf-8") as f:
                translated_content = f.read()

            # Extract existing metadata from translated file
            metadata = extract_metadata_from_content(translated_content)
            if not metadata:
                logger.warning(f"No metadata found in {translated_file}")
                return {}, False

            # Initialize evaluation results
            rule_based_result = {"confidence_score": 1.0, "issues_found": []}

            # Perform rule-based evaluation if enabled
            if self.use_rule:
                logger.info(f"Performing rule-based evaluation for {translated_file}")
                rule_based_result = evaluate_translation_rule_based(
                    original_content, translated_content, language_code
                )
            else:
                logger.info(f"Skipping rule-based evaluation for {translated_file}")

            # If LLM is enabled, perform chunk-based evaluation
            chunk_evaluations = []
            if self.use_llm:
                # First handle code blocks to prevent them from being evaluated
                orig_no_code, orig_code_map = replace_code_blocks_and_inline_code(
                    original_content
                )
                trans_no_code, trans_code_map = replace_code_blocks_and_inline_code(
                    translated_content
                )

                # Use LLM for evaluation if use_llm is enabled
                logger.info(f"Performing LLM-based evaluation for {translated_file}")
                try:
                    # Split into chunks (using same logic as in translation)
                    orig_chunks = process_markdown(orig_no_code, max_tokens)
                    trans_chunks = process_markdown(trans_no_code, max_tokens)

                    # Make sure we have the same number of chunks
                    min_chunks = min(len(orig_chunks), len(trans_chunks))

                    logger.info(
                        f"LLM Evaluation: Processing {min_chunks} chunks in {translated_file.name}"
                    )

                    # Evaluate each chunk pair
                    for i in range(min_chunks):
                        orig_chunk = orig_chunks[i]
                        trans_chunk = trans_chunks[i]

                        # Generate evaluation prompt for this chunk
                        prompt = generate_evaluation_prompt(
                            orig_chunk, trans_chunk, language_code
                        )

                        # Get evaluation from LLM
                        logger.debug(
                            f"Sending chunk {i+1}/{min_chunks} to LLM for evaluation"
                        )
                        llm_response = await self._run_prompt(prompt, i + 1, min_chunks)

                        # Parse response
                        try:
                            if llm_response:
                                chunk_result = json.loads(llm_response)
                                chunk_result["chunk_index"] = (
                                    i  # Track which chunk had issues
                                )
                                chunk_evaluations.append(chunk_result)

                                # Log progress
                                if (
                                    i + 1
                                ) % 5 == 0 or i + 1 == min_chunks:  # Log every 5 chunks or at the end
                                    logger.info(
                                        f"Evaluated chunk {i+1}/{min_chunks} for {translated_file.name}"
                                    )
                        except json.JSONDecodeError:
                            logger.warning(
                                f"Failed to parse LLM response for chunk {i}: {llm_response[:100]}..."
                            )

                    # Log completion
                    logger.info(
                        f"Completed LLM evaluation of all {min_chunks} chunks in {translated_file.name}"
                    )

                    # Check for mismatch in number of chunks
                    if len(orig_chunks) != len(trans_chunks):
                        chunk_issue = {
                            "confidence_score": 0.3,
                            "issues_found": [
                                "Chunk count mismatch between original and translated content"
                            ],
                            "chunk_index": -1,  # Special index to indicate a global issue
                        }
                        chunk_evaluations.append(chunk_issue)
                except Exception as e:
                    logger.error(f"Error during LLM evaluation: {e}")

                # Also check code blocks preservation
                if orig_code_map.keys() != trans_code_map.keys():
                    code_issue = {
                        "confidence_score": 0.4,
                        "issues_found": [
                            "Code block count mismatch between original and translated content"
                        ],
                        "chunk_index": -1,
                    }
                    chunk_evaluations.append(code_issue)

            # Combine rule-based and chunk-based evaluations
            evaluation_result = self._combine_chunk_evaluations(
                rule_based_result, chunk_evaluations
            )

            # Update metadata with evaluation
            metadata["evaluation"] = evaluation_result

            # Format updated metadata
            metadata_comment = format_metadata_comment(metadata)

            # Update the file with new metadata
            # First, remove old metadata comment and add new one
            content_parts = translated_content.split("\n\n", 1)
            if len(content_parts) > 1:
                updated_content = metadata_comment + content_parts[1]
            else:
                # If splitting fails, preserve content but add new metadata
                updated_content = metadata_comment + translated_content.replace(
                    content_parts[0], ""
                )

            # Write back to file
            with open(translated_file, "w", encoding="utf-8") as f:
                f.write(updated_content)

            logger.info(f"Updated evaluation metadata for {translated_file}")
            return evaluation_result, True

        except Exception as e:
            logger.error(f"Error evaluating {translated_file}: {e}")
            return {}, False

    def _combine_chunk_evaluations(
        self, rule_based: Dict, chunk_evaluations: List[Dict]
    ) -> Dict:
        """
        Combine rule-based evaluation with chunk-based LLM evaluations.

        Args:
            rule_based: Results from rule-based evaluation of the whole document
            chunk_evaluations: List of evaluation results for each chunk

        Returns:
            Combined evaluation results dictionary
        """
        combined = rule_based.copy()  # Start with rule-based results

        # If we have chunk evaluations, enhance the overall evaluation
        if chunk_evaluations:
            # Collect all issues from all chunks
            all_issues = set(combined.get("issues", []))

            # Track chunk confidence scores
            chunk_scores = []

            for chunk_eval in chunk_evaluations:
                # Add issues from this chunk
                if "issues_found" in chunk_eval:
                    for issue in chunk_eval["issues_found"]:
                        # Add chunk index to the issue if available
                        if "chunk_index" in chunk_eval:
                            issue_text = f"{issue} (chunk {chunk_eval['chunk_index']})"
                        else:
                            issue_text = issue
                        all_issues.add(issue_text)

                # Track confidence score
                if "confidence_score" in chunk_eval:
                    chunk_scores.append(chunk_eval["confidence_score"])

            # Calculate weighted average of confidence scores
            if chunk_scores:
                # Rule-based score
                rule_confidence = combined.get("confidence_score", 0.5)

                # Find the minimum chunk score (worst chunk)
                min_chunk_score = min(chunk_scores)

                # Average of all chunk scores
                avg_chunk_score = sum(chunk_scores) / len(chunk_scores)

                # Weighted average with bias towards lower scores (more conservative)
                # 40% weight to worst chunk, 30% to rule-based, 30% to average of chunks
                weighted_score = (
                    min_chunk_score * 0.4
                    + rule_confidence * 0.3
                    + avg_chunk_score * 0.3
                )

                combined["confidence_score"] = round(weighted_score, 2)
                combined["chunk_scores"] = chunk_scores

            # Update issues list
            combined["issues"] = list(all_issues)

            # Add summary of chunk evaluation
            summary = f"Evaluated {len(chunk_evaluations)} chunks. "
            if chunk_scores:
                worst_chunk_idx = chunk_scores.index(min(chunk_scores))
                summary += f"Lowest confidence in chunk {worst_chunk_idx}."
                combined["worst_chunk"] = worst_chunk_idx

            combined["summary"] = summary

        return combined

    def get_evaluation_summary(self, evaluation_results: Dict) -> str:
        """
        Generate a human-readable summary of the evaluation results.

        Args:
            evaluation_results: Dictionary containing evaluation results

        Returns:
            A formatted string summarizing the evaluation
        """
        if not evaluation_results:
            return "No evaluation data available."

        confidence = evaluation_results.get("confidence_score", 0.0)
        issues = evaluation_results.get("issues", [])
        summary = evaluation_results.get("summary", "")
        llm_summary = evaluation_results.get("llm_summary", "")

        result = f"Confidence Score: {confidence:.2f}\n"

        # Add LLM ratings if available
        rating_keys = [
            "completeness_rating",
            "accuracy_rating",
            "language_consistency_rating",
            "markdown_structure_rating",
        ]
        ratings_available = any(k in evaluation_results for k in rating_keys)

        if ratings_available:
            result += "\nDetailed Ratings:\n"
            for key in rating_keys:
                if key in evaluation_results:
                    # Format the key for display (remove _rating and capitalize words)
                    display_name = key.replace("_rating", "").replace("_", " ").title()
                    result += f"- {display_name}: {evaluation_results[key]:.2f}\n"

        if issues:
            result += "\nIssues Found:\n"
            for issue in issues:
                result += f"- {issue}\n"
        else:
            result += "\nNo issues detected.\n"

        if llm_summary:
            result += f"\nLLM Evaluation: {llm_summary}\n"

        if summary:
            result += f"\nSummary: {summary}"

        return result
