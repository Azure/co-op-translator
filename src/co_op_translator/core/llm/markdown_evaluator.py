"""
This module provides functionality to evaluate the quality of markdown translations.
"""

import asyncio
import json
import logging
from pathlib import Path
from typing import Dict, Optional, Tuple, List, Any

from co_op_translator.utils.common.metadata_utils import (
    evaluate_translation,
    extract_metadata_from_content,
    format_metadata_comment
)
from co_op_translator.utils.llm.markdown_utils import (
    generate_evaluation_prompt,
    process_markdown,
    replace_code_blocks_and_inline_code,
    restore_code_blocks_and_inline_code
)
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.llm_config.provider import LLMProvider

logger = logging.getLogger(__name__)


class MarkdownEvaluator:
    """
    Class for evaluating the quality of markdown translations.
    
    This class provides methods to analyze translations, calculate confidence scores,
    and update metadata with evaluation results. It supports both rule-based evaluation
    and LLM-based evaluation when an LLM provider is configured.
    """
    
    def __init__(self, root_dir: Optional[Path] = None, use_llm: bool = False, llm_config: Optional[Dict] = None):
        """
        Initialize the markdown evaluator.
        
        Args:
            root_dir: Root directory of the project for path calculations
            use_llm: Whether to use LLM for enhanced evaluation (if available)
            llm_config: Configuration for the LLM provider (if use_llm is True)
        """
        self.root_dir = root_dir
        self.use_llm = use_llm
        self.llm_provider = None
        
        # Initialize LLM provider if requested
        if use_llm and llm_config:
            try:
                config = LLMConfig(**llm_config)
                self.llm_provider = LLMProvider(config)
                logger.info("LLM provider initialized for enhanced translation evaluation")
            except Exception as e:
                logger.warning(f"Failed to initialize LLM provider for evaluation: {e}")
                self.use_llm = False
    
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
            with open(original_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
                
            with open(translated_file, 'r', encoding='utf-8') as f:
                translated_content = f.read()
            
            # Extract existing metadata from translated file
            metadata = extract_metadata_from_content(translated_content)
            if not metadata:
                logger.warning(f"No metadata found in {translated_file}")
                return {}, False
            
            # First perform rule-based evaluation on the entire content
            rule_based_result = evaluate_translation(
                original_content,
                translated_content,
                language_code
            )
            
            # If LLM is enabled, perform chunk-based evaluation
            chunk_evaluations = []
            if self.use_llm and self.llm_provider:
                try:
                    # First handle code blocks to prevent them from being evaluated
                    orig_no_code, orig_code_map = replace_code_blocks_and_inline_code(original_content)
                    trans_no_code, trans_code_map = replace_code_blocks_and_inline_code(translated_content)
                    
                    # Split into chunks (using same logic as in translation)
                    orig_chunks = process_markdown(orig_no_code, max_tokens)
                    trans_chunks = process_markdown(trans_no_code, max_tokens)
                    
                    # Make sure we have the same number of chunks
                    min_chunks = min(len(orig_chunks), len(trans_chunks))
                    
                    # Evaluate each chunk pair
                    for i in range(min_chunks):
                        orig_chunk = orig_chunks[i]
                        trans_chunk = trans_chunks[i]
                        
                        # Generate evaluation prompt for this chunk
                        prompt = generate_evaluation_prompt(
                            orig_chunk, 
                            trans_chunk, 
                            language_code
                        )
                        
                        # Get evaluation from LLM
                        llm_response = await self.llm_provider.generate_text(prompt)
                        
                        # Parse response
                        try:
                            if llm_response:
                                chunk_result = json.loads(llm_response)
                                chunk_result['chunk_index'] = i  # Track which chunk had issues
                                chunk_evaluations.append(chunk_result)
                                logger.info(f"Evaluated chunk {i+1}/{min_chunks} for {translated_file}")
                        except json.JSONDecodeError:
                            logger.warning(f"Failed to parse LLM response for chunk {i}: {llm_response[:100]}...")
                    
                    # Check for mismatch in number of chunks
                    if len(orig_chunks) != len(trans_chunks):
                        chunk_issue = {
                            "confidence_score": 0.3,
                            "issues_found": ["Chunk count mismatch between original and translated content"],
                            "chunk_index": -1  # Special index to indicate a global issue
                        }
                        chunk_evaluations.append(chunk_issue)
                    
                    # Also check code blocks preservation
                    if orig_code_map.keys() != trans_code_map.keys():
                        code_issue = {
                            "confidence_score": 0.4,
                            "issues_found": ["Code block count mismatch between original and translated content"],
                            "chunk_index": -1
                        }
                        chunk_evaluations.append(code_issue)
                    
                except Exception as e:
                    logger.error(f"Error during chunk-based evaluation: {e}")
            
            # Combine rule-based and chunk-based evaluations
            evaluation_result = self._combine_chunk_evaluations(rule_based_result, chunk_evaluations)
            
            # Update metadata with evaluation
            metadata["evaluation"] = evaluation_result
            
            # Format updated metadata
            metadata_comment = format_metadata_comment(metadata)
            
            # Update the file with new metadata
            # First, remove old metadata comment and add new one
            content_parts = translated_content.split('\n\n', 1)
            if len(content_parts) > 1:
                updated_content = metadata_comment + content_parts[1]
            else:
                # If splitting fails, preserve content but add new metadata
                updated_content = metadata_comment + translated_content.replace(
                    content_parts[0], ''
                )
            
            # Write back to file
            with open(translated_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            logger.info(f"Updated evaluation metadata for {translated_file}")
            return evaluation_result, True
            
        except Exception as e:
            logger.error(f"Error evaluating {translated_file}: {e}")
            return {}, False
    
    def _combine_chunk_evaluations(self, rule_based: Dict, chunk_evaluations: List[Dict]) -> Dict:
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
                    min_chunk_score * 0.4 + 
                    rule_confidence * 0.3 + 
                    avg_chunk_score * 0.3
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
        rating_keys = ["completeness_rating", "accuracy_rating", 
                      "language_consistency_rating", "markdown_structure_rating"]
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
