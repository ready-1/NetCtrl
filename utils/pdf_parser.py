"""
PDF Parser Utility
Converts PDF manuals into searchable chapter-based text files.
"""

import pdfplumber
import json
import re
from pathlib import Path
import logging
from typing import Dict, List, Tuple
import os
import hashlib


class PDFParser:
    def __init__(self, pdf_path: str, output_dir: str):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.chapters: Dict[str, Dict] = {}
        self.current_chapter = ""
        self.setup_logging()

    def setup_logging(self):
        """Configure logging for the parser."""
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger(__name__)

    def clean_title(self, title: str) -> str:
        """Clean and normalize a chapter title to create a valid filename.

        Args:
            title: The raw chapter title text

        Returns:
            A cleaned title string suitable for use as a filename
        """
        # Remove any leading/trailing whitespace
        title = title.strip()

        # Convert to lowercase
        title = title.lower()

        # Replace problematic characters with underscores
        title = re.sub(r"[^\w\s-]", "_", title)

        # Replace whitespace with underscores
        title = re.sub(r"\s+", "_", title)

        # Remove consecutive underscores
        title = re.sub(r"_+", "_", title)

        # Remove leading/trailing underscores
        title = title.strip("_")

        # Truncate if too long and add hash of original
        if len(title) > 100:
            hash_suffix = hashlib.md5(title.encode()).hexdigest()[:8]
            title = title[:90] + "_" + hash_suffix

        return title

    def extract_chapter_title(self, text: str) -> str:
        """Extract chapter title from text using regex patterns."""
        # Common chapter patterns in technical manuals
        patterns = [
            # Match "Chapter X - Title" or "Chapter X. Title"
            r"^Chapter\s+\d+\s*[-–—.]\s*([A-Z][^\n]+)$",
            # Match "X. Title" or "X.Y Title"
            r"^\d+(?:\.\d+)*\s+([A-Z][^\n]+)$",
            # Match all caps section titles
            r"^([A-Z][A-Z\s]+(?:\s+[A-Za-z][\w\s-]+)?)$",
            # Match "TITLE (description)" format
            r"^([A-Z][A-Z\s]+(?:\s*\([^)]+\))?)$",
        ]

        for pattern in patterns:
            if match := re.search(pattern, text, re.MULTILINE):
                return self.clean_title(match.group(1))
        return ""

    def is_new_chapter(self, text: str) -> bool:
        """Determine if text starts a new chapter."""
        chapter_indicators = [
            r"^Chapter\s+\d+\s*[-–—.]",  # Chapter numbers with separator
            r"^\d+(?:\.\d+)*\s+[A-Z]",  # Section numbers
            r"^[A-Z][A-Z\s]+(?:\s+[A-Za-z][\w\s-]+)?$",  # All caps titles
            r"^[A-Z][A-Z\s]+(?:\s*\([^)]+\))?$",  # ALL CAPS with description
        ]
        return any(
            re.search(pattern, text, re.MULTILINE) for pattern in chapter_indicators
        )

    def clean_text(self, text: str) -> str:
        """Clean extracted text by removing headers, footers, and extra whitespace."""
        # Remove common headers/footers
        text = re.sub(r"Page \d+ of \d+", "", text)
        text = re.sub(r"NETGEAR M4300", "", text)
        text = re.sub(r"CLI Command Reference Manual", "", text)
        text = re.sub(r"Copyright NETGEAR.*$", "", text, flags=re.MULTILINE)
        text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)  # Page numbers

        # Remove duplicate newlines and whitespace
        text = re.sub(r"\s*\n\s*\n\s*", "\n\n", text)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n[ \t]+", "\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)

        # Remove empty lines at start/end
        text = text.strip()

        return text

    def process_page(self, page_text: str, page_num: int) -> None:
        """Process a single page of text."""
        cleaned_text = self.clean_text(page_text)

        if self.is_new_chapter(cleaned_text):
            chapter_title = self.extract_chapter_title(cleaned_text)
            if chapter_title:
                self.current_chapter = chapter_title
                self.chapters[chapter_title] = {
                    "content": cleaned_text,
                    "start_page": page_num,
                    "end_page": page_num,
                    "sections": {},
                }
        elif self.current_chapter:
            # Update existing chapter
            self.chapters[self.current_chapter]["content"] += f"\n\n{cleaned_text}"
            self.chapters[self.current_chapter]["end_page"] = page_num

            # Try to identify sections within chapters
            section_matches = re.finditer(r"\n(\d+\.\d+\s+[A-Z][^\n]+)", cleaned_text)
            for match in section_matches:
                section_title = match.group(1).strip()
                self.chapters[self.current_chapter]["sections"][
                    section_title
                ] = page_num

    def parse_pdf(self) -> None:
        """Parse the PDF and extract chapters."""
        self.logger.info(f"Processing PDF: {self.pdf_path}")

        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                total_pages = len(pdf.pages)
                self.logger.info(f"PDF has {total_pages} pages")

                for page_num, page in enumerate(pdf.pages, 1):
                    self.logger.info(f"Processing page {page_num} of {total_pages}")
                    text = page.extract_text()
                    if text:
                        self.process_page(text, page_num)

            self.logger.info(f"Successfully processed {total_pages} pages")
            self.logger.info(f"Found {len(self.chapters)} chapters")

        except Exception as e:
            self.logger.error(f"Error processing PDF: {str(e)}")
            raise

    def save_chapters(self) -> None:
        """Save extracted chapters to individual files."""
        # Create output directory
        chapters_dir = self.output_dir
        chapters_dir.mkdir(parents=True, exist_ok=True)

        # Save chapter index with sections
        index = {
            name: {
                "file": f"{self._sanitize_filename(name)}.md",
                "start_page": info["start_page"],
                "end_page": info["end_page"],
                "sections": info["sections"],
            }
            for name, info in self.chapters.items()
        }

        # Save index file
        with open(chapters_dir / "index.json", "w") as f:
            json.dump(index, f, indent=2)

        # Save individual chapters
        for name, info in self.chapters.items():
            filename = chapters_dir / f"{self._sanitize_filename(name)}.md"
            with open(filename, "w") as f:
                # Write chapter header
                f.write(f"# {name}\n\n")
                f.write(f"Pages: {info['start_page']}-{info['end_page']}\n\n")

                # Write sections index if available
                if info["sections"]:
                    f.write("## Sections\n\n")
                    for section, page in info["sections"].items():
                        f.write(f"- {section} (Page {page})\n")
                    f.write("\n")

                # Write main content
                f.write("## Content\n\n")
                f.write(info["content"])

        self.logger.info(f"Saved {len(self.chapters)} chapters to {chapters_dir}")

    def _sanitize_filename(self, filename: str) -> str:
        """Convert chapter title to valid filename."""
        # Remove invalid characters and convert spaces to underscores
        clean = re.sub(r"[^\w\s-]", "", filename)
        return clean.strip().replace(" ", "_").lower()


def create_parser(pdf_path: str, output_dir: str) -> PDFParser:
    """Create a new PDFParser instance."""
    return PDFParser(pdf_path, output_dir)
