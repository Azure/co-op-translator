from __future__ import annotations

from pathlib import Path
import shutil


def read_input_file(input_file: str | Path) -> str:
    """
    Read the content of an input file and return it as a stripped string.

    Args:
        input_file (str | Path): The path to the input file.

    Returns:
        str: The stripped content of the file.
    """
    input_file = Path(input_file)
    with input_file.open("r", encoding="utf-8") as file:
        return file.read().strip()


def handle_empty_document(input_file: str | Path, output_file: str | Path) -> None:
    """
    Copy the input file to the output location if the document is empty.

    Args:
        input_file (str | Path): The path to the input file.
        output_file (str | Path): The path to the output file.
    """
    input_file = Path(input_file)
    output_file = Path(output_file)
    shutil.copyfile(input_file, output_file)


def write_output_file(output_file: str | Path, results: list) -> None:
    """
    Write a list of results to the output file, each on a new line.

    Args:
        output_file (str | Path): The path to the output file.
        results (list): A list of strings to write to the file.
    """
    output_file = Path(output_file)
    with output_file.open("w", encoding="utf-8") as text_file:
        for result in results:
            text_file.write(result)
            text_file.write("\n")
