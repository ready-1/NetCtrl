"""
Template filters for working with Markdown content in Django templates.

This module provides filters for:
- Converting Markdown to HTML with proper sanitization
- Escaping HTML content
- Converting plaintext to HTML with proper line breaks
"""

import markdown
import bleach
import logging
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

# Set up module logger
logger = logging.getLogger(__name__)

# Try to import CSS sanitizer
try:
    from bleach.css_sanitizer import CSSSanitizer
    CSS_SANITIZER_AVAILABLE = True
except ImportError:
    logger.warning("bleach.css_sanitizer.CSSSanitizer not available - CSS sanitization will be limited")
    CSS_SANITIZER_AVAILABLE = False

register = template.Library()

# Allowable HTML tags for markdown rendering
ALLOWED_TAGS = [
    'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'ul',
    'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'br', 'strong', 'pre', 'span',
    'table', 'thead', 'tbody', 'tr', 'th', 'td', 'div', 'img'
]

# Allowable HTML attributes
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title', 'target', 'rel'],
    'abbr': ['title'],
    'acronym': ['title'],
    'img': ['src', 'alt', 'title', 'width', 'height'],
    'table': ['border', 'cellpadding', 'cellspacing', 'class'],
    'th': ['scope', 'colspan', 'rowspan', 'class'],
    'td': ['colspan', 'rowspan', 'class'],
    '*': ['class', 'id', 'style']
}

# Allowable CSS properties
ALLOWED_STYLES = [
    'color', 'background-color', 'font-family', 'font-size', 'font-weight',
    'text-align', 'text-decoration', 'border', 'padding', 'margin', 'width',
    'height', 'display'
]

@register.filter(name='markdown_to_html')
def markdown_to_html(markdown_text):
    """
    Convert markdown text to sanitized HTML.
    
    This filter handles the conversion from markdown to HTML, and also
    sanitizes the HTML to prevent XSS attacks.
    
    Args:
        markdown_text (str): The markdown text to convert.
        
    Returns:
        str: Sanitized HTML string marked as safe.
    """
    if not markdown_text:
        return ''
    
    # Convert markdown to HTML using the Python-Markdown library
    try:
        # Use extensions to support tables, code highlighting, etc.
        html = markdown.markdown(
            markdown_text,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.smarty',
                'markdown.extensions.tables',
                'markdown.extensions.toc'
            ]
        )
        
        # Set up CSS sanitizer if available
        css_sanitizer = None
        if CSS_SANITIZER_AVAILABLE:
            css_sanitizer = CSSSanitizer(allowed_css_properties=ALLOWED_STYLES)
        
        # Sanitize the HTML with proper CSS handling
        try:
            # Modern bleach with CSSSanitizer
            if css_sanitizer:
                clean_html = bleach.clean(
                    html,
                    tags=ALLOWED_TAGS,
                    attributes=ALLOWED_ATTRIBUTES,
                    css_sanitizer=css_sanitizer,
                    strip=True
                )
            else:
                # Using styles parameter for older bleach versions that don't support css_sanitizer
                clean_html = bleach.clean(
                    html,
                    tags=ALLOWED_TAGS,
                    attributes=ALLOWED_ATTRIBUTES,
                    styles=ALLOWED_STYLES,
                    strip=True
                )
        except TypeError as e:
            # Last resort fallback: handle the case where neither method works
            logger.warning(f"CSS sanitization failed: {e}. Falling back to basic HTML sanitization.")
            
            # Remove style attribute from allowed attributes to avoid warnings
            modified_attributes = ALLOWED_ATTRIBUTES.copy()
            for key in modified_attributes:
                if 'style' in modified_attributes[key]:
                    modified_attributes[key] = [attr for attr in modified_attributes[key] if attr != 'style']
            
            clean_html = bleach.clean(
                html,
                tags=ALLOWED_TAGS,
                attributes=modified_attributes,
                strip=True
            )
        
        return mark_safe(clean_html)
    except Exception as e:
        # Log the error and return a sanitized version of the markdown text
        logger.error(f"Error converting markdown to HTML: {e}")
        return mark_safe(f'<pre>{escape(markdown_text)}</pre>')


@register.filter(name='plaintext_to_html')
def plaintext_to_html(text):
    """
    Convert plain text to HTML with line breaks.
    
    Args:
        text (str): The plain text to convert.
        
    Returns:
        str: HTML string with paragraphs and line breaks, marked as safe.
    """
    if not text:
        return ''
    
    # Escape HTML
    escaped_text = escape(text)
    
    # Convert line breaks to HTML breaks
    paragraphs = escaped_text.split('\n\n')
    processed_paragraphs = []
    
    for p in paragraphs:
        if p.strip():
            p = p.replace('\n', '<br>')
            processed_paragraphs.append(f'<p>{p}</p>')
    
    return mark_safe('\n'.join(processed_paragraphs))


@register.filter(name='render_document_content')
def render_document_content(document):
    """
    Render document content based on its content format.
    
    This is a convenience filter that handles both markdown and plaintext formats.
    
    Args:
        document: A Document instance with content and content_format attributes.
        
    Returns:
        str: HTML string marked as safe.
    """
    if not document or not hasattr(document, 'content') or not document.content:
        return ''
    
    if not hasattr(document, 'content_format'):
        # Default to markdown if no format specified
        return markdown_to_html(document.content)
    
    if document.content_format == 'markdown':
        return markdown_to_html(document.content)
    elif document.content_format == 'plaintext':
        return plaintext_to_html(document.content)
    else:
        # Fallback if format not recognized
        return plaintext_to_html(document.content)
