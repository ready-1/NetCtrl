"""
Integration tests for Markdown rendering in the NetCtrl CMS.

These tests verify that:
1. Markdown content is correctly rendered to HTML
2. HTML sanitization is working properly
3. Plain text content is properly formatted with paragraphs and line breaks
"""

import os
import sys
import django
import unittest

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netctrl.settings')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
django.setup()

from django.test import TestCase
from cms.templatetags.markdown_filters import markdown_to_html, plaintext_to_html, render_document_content
from cms.models.documents import Document


class MockDocument:
    """Mock document class for testing the render_document_content filter."""
    
    def __init__(self, content, content_format):
        self.content = content
        self.content_format = content_format


class MarkdownRenderingTests(TestCase):
    """Tests for the Markdown rendering functionality."""
    
    def test_markdown_to_html_basic(self):
        """Test basic Markdown conversion."""
        markdown_text = "# Heading\n\nThis is a paragraph with **bold** and *italic* text."
        html = markdown_to_html(markdown_text)
        
        self.assertIn('<h1>Heading</h1>', html)
        self.assertIn('<strong>bold</strong>', html)
        self.assertIn('<em>italic</em>', html)
    
    def test_markdown_to_html_sanitization(self):
        """Test that HTML sanitization is working properly."""
        # HTML with potential XSS
        dangerous_markdown = """
# Safe Heading

<script>alert('XSS');</script>

<a href="javascript:alert('XSS')">Click me</a>

<iframe src="https://evil.com"></iframe>
"""
        html = markdown_to_html(dangerous_markdown)
        
        # Check that heading is preserved
        self.assertIn('<h1>Safe Heading</h1>', html)
        
        # Check that dangerous elements are removed
        self.assertNotIn('<script>', html)
        self.assertNotIn('javascript:', html)
        self.assertNotIn('<iframe', html)
    
    def test_markdown_to_html_complex(self):
        """Test more complex Markdown features."""
        complex_markdown = """
# Complex Markdown Test

## Lists

* Unordered item 1
* Unordered item 2
  * Nested item
  
1. Ordered item 1
2. Ordered item 2

## Code

Inline `code` example.

```python
def example():
    return "This is Python code"
```

## Tables

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |

"""
        html = markdown_to_html(complex_markdown)
        
        # Check that complex features are rendered
        self.assertIn('<h1>Complex Markdown Test</h1>', html)
        self.assertIn('<ul>', html)
        self.assertIn('<ol>', html)
        self.assertIn('<code>', html)
        self.assertIn('<table>', html)
        self.assertIn('<th>', html)
        self.assertIn('<td>', html)
    
    def test_plaintext_to_html(self):
        """Test plain text conversion to HTML."""
        plain_text = "Line 1\nLine 2\n\nParagraph 2\nWith another line"
        html = plaintext_to_html(plain_text)
        
        # Check that paragraphs are created
        self.assertIn('<p>Line 1<br>Line 2</p>', html)
        self.assertIn('<p>Paragraph 2<br>With another line</p>', html)
        
        # Check HTML escaping
        special_text = "Text with <script> & symbols"
        html = plaintext_to_html(special_text)
        self.assertIn('&lt;script&gt;', html)
        self.assertIn('&amp;', html)
    
    def test_render_document_content_markdown(self):
        """Test rendering Markdown document content."""
        doc = MockDocument("# Test\n\nContent", "markdown")
        html = render_document_content(doc)
        
        self.assertIn('<h1>Test</h1>', html)
    
    def test_render_document_content_plaintext(self):
        """Test rendering plain text document content."""
        doc = MockDocument("Line 1\n\nLine 2", "plaintext")
        html = render_document_content(doc)
        
        self.assertIn('<p>Line 1</p>', html)
        self.assertIn('<p>Line 2</p>', html)
    
    def test_render_document_content_fallback(self):
        """Test rendering with unknown format."""
        doc = MockDocument("Content", "unknown")
        html = render_document_content(doc)
        
        # Should fall back to plain text
        self.assertIn('<p>Content</p>', html)
    
    def test_empty_input(self):
        """Test empty input handling."""
        self.assertEqual(markdown_to_html(""), "")
        self.assertEqual(plaintext_to_html(""), "")
        self.assertEqual(render_document_content(None), "")
        self.assertEqual(render_document_content(MockDocument("", "markdown")), "")


if __name__ == '__main__':
    unittest.main()
