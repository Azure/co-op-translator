"""
Main entry point for the Co-op Translator CLI.
This module provides command dispatching for both 'translate' and 'evaluate' commands.
"""

import sys
import logging
from pathlib import Path

from co_op_translator.cli.translate import translate_command
from co_op_translator.cli.evaluate import evaluate_command
from co_op_translator.cli.migrate_links import migrate_links_command
from co_op_translator.cli.review import review_command

logger = logging.getLogger(__name__)


def main():
    """
    Main entry point function that routes to the appropriate command.
    This function is used by the command-line scripts.
    """
    script_name = Path(sys.argv[0]).stem
    if script_name == "evaluate":
        evaluate_command()
    elif script_name == "migrate-links":
        migrate_links_command()
    elif script_name == "co-op-review":
        review_command()
    else:
        translate_command()


if __name__ == "__main__":
    main()
