from __future__ import annotations

import re


def extract_json_from_markdown_codeblock(response: str) -> str:
    """
    Extract JSON content from markdown code blocks.

    Extracts JSON formatted as markdown code blocks (```json) from LLM responses.

    Args:
        response (str): Original response text from the LLM

    Returns:
        str: Cleaned JSON string with markdown formatting removed
    """
    cleaned_response = response

    # Check if the response starts with a markdown code block
    if cleaned_response.strip().startswith("```"):
        # Extract content between the first and last code block markers
        parts = cleaned_response.split("```", 2)
        if len(parts) >= 3:
            # If the format is ```json\n{...}\n```, take the middle part
            json_content = parts[1]
            # Remove language identifier if present
            if "\n" in json_content:
                json_content = json_content.split("\n", 1)[1]
            cleaned_response = json_content
        else:
            # Handle cases where closing ``` might be missing
            if cleaned_response.strip().startswith("```json"):
                cleaned_response = cleaned_response.replace("```json", "", 1).strip()
            elif cleaned_response.strip().startswith("```"):
                cleaned_response = cleaned_response.replace("```", "", 1).strip()

    return cleaned_response


def generate_evaluation_prompt(
    original_content: str,
    translated_content: str,
    language_code: str,
    language_name: str,
) -> str:
    """
    Generate a prompt for LLM to evaluate translation quality.

    This prompt asks the LLM to evaluate a translation by comparing the original and translated content
    and identifying issues related to completeness, accuracy, language consistency, and preservation of
    markdown structure.

    Args:
        original_content (str): The original markdown content
        translated_content (str): The translated markdown content
        language_code (str): The target language code of the translation
        language_name (str): The target language name of the translation

    Returns:
        str: A prompt for the LLM to evaluate the translation quality
    """
    # Remove metadata comments from translated content to ensure fair comparison
    clean_translated = re.sub(
        r"<!--\s*CO_OP_TRANSLATOR_METADATA:[\s\S]*?-->", "", translated_content
    )

    # Using full content for evaluation since the chunks are already limited to 2048 tokens
    original_sample = original_content
    translated_sample = clean_translated

    # Create the evaluation prompt
    disclaimer_instruction = """
IMPORTANT: The translated text includes an automatically generated disclaimer at the end that is not part of the original content.
This disclaimer typically starts with bold text (e.g., '**Disclaimer**') and contains information about the machine translation.
When evaluating EXCLUDE this disclaimer from your comparison and evaluation
"""

    prompt = f"""You are a professional translation quality evaluator specializing in {language_name} ({language_code}) translations.

    I will provide you with an original text and its translation to {language_name} ({language_code}).
    Please evaluate the translation quality and identify specific issues.

    For each issue you find, provide:
    1. A clear description of the issue
    2. A severity score from 0.0 to 1.0 where:
       - 0.0-0.2: Minor issues (typos, minor style inconsistencies)
       - 0.3-0.4: Moderate issues (unclear phrasing, minor meaning changes)
       - 0.5-0.6: Significant issues (noticeable meaning changes, grammar errors)
       - 0.7-0.8: Major issues (substantial meaning errors, missing content)
       - 0.9-1.0: Critical issues (completely wrong meaning, missing major sections)

    Also evaluate these criteria on a scale of 0-10:
    1. COMPLETENESS: Are all sections from the original present in the translation?
    2. ACCURACY: Is the meaning of the original accurately conveyed?
    3. LANGUAGE CONSISTENCY: Is the target language ({language_name}) used consistently throughout?
    4. MARKDOWN STRUCTURE: Are markdown elements (headings, links, lists) preserved?

    Calculate an overall confidence score from 0 to 1.0 based on these criteria.

    {disclaimer_instruction}

    ORIGINAL CONTENT SAMPLE:
    ```
    {original_sample}
    ```

    TRANSLATED CONTENT SAMPLE ({language_name} - {language_code}):
    ```
    {translated_sample}
    ```

    Format your response as a JSON object with the following structure:
    {{
        "completeness_score": 0-10,
        "accuracy_score": 0-10,
        "language_consistency_score": 0-10,
        "markdown_structure_score": 0-10,
        "issues_found": [
            {{
                "description": "Clear description of the issue",
                "severity": 0.0-1.0,
                "location": "Where the issue occurs (optional)",
                "impact": "Brief explanation of why this issue matters"
            }}
        ],
        "max_issue_severity": 0.0-1.0,
        "confidence_score": 0.0-1.0,
        "evaluation_summary": "A brief summary of your evaluation."
    }}

    IMPORTANT: Focus on providing accurate severity scores for each issue. The system will use these scores to determine if retranslation is needed.
    """

    return prompt
