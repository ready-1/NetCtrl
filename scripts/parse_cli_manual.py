#!/usr/bin/env python3

"""Script to parse the CLI manual PDF into markdown files."""

import os
import sys
import re
import json
from pathlib import Path
from typing import Union

# Add project root to Python path before importing local modules
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Now we can safely import our local module
from utils.pdf_parser import create_parser


def main() -> None:
    """Parse the CLI manual PDF and save chapters as markdown files."""
    # Configure paths
    pdf_path = PROJECT_ROOT / "docs/netgear_swagger/M4300-M4300-96X_CLI_EN.pdf"
    output_dir = PROJECT_ROOT / "docs/cli_manual"

    # Ensure the PDF exists
    if not pdf_path.exists():
        print("Error: CLI manual not found at {}".format(pdf_path))
        sys.exit(1)

    try:
        # Parse the PDF
        parser = create_parser(str(pdf_path), str(output_dir))
        parser.parse_pdf()
        print("Processing CLI manual...")
        parser.save_chapters()

        print("\nSuccessfully parsed CLI manual!")
        print("Output directory: {}".format(output_dir))
        print("\nYou can now search through the manual chapters in markdown format.")

    except Exception as e:
        print("Error parsing CLI manual: {}".format(str(e)))
        sys.exit(1)


if __name__ == "__main__":
    main()
