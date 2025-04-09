#!/usr/bin/env python
"""
Bleach CSS Sanitizer test script.

This script demonstrates and tests the Bleach CSS sanitizer functionality,
which is used in NetCtrl's Markdown rendering.
"""
import sys
import bleach
from pathlib import Path

# Add the app directory to the Python path
script_dir = Path(__file__).resolve().parent
app_dir = script_dir.parent / 'app'
sys.path.insert(0, str(app_dir))

def test_css_sanitizer():
    """Test the Bleach CSS sanitizer functionality"""
    print("Bleach CSS Sanitizer Test")
    print("========================")
    
    try:
        # Import the CSS sanitizer
        from bleach.css_sanitizer import CSSSanitizer
        print("✓ Successfully imported CSS sanitizer")
        
        # Test 1: Create a sanitizer with allowed CSS properties
        allowed_css_props = ['color', 'background-color', 'font-size', 'text-align']
        css_sanitizer = CSSSanitizer(allowed_css_properties=allowed_css_props)
        print(f"✓ Successfully created CSS sanitizer with allowed properties: {', '.join(allowed_css_props)}")
        
        # Test 2: Sanitize HTML with allowed CSS
        html_with_allowed_css = '<p style="color: blue; font-size: 16px;">This text has allowed CSS</p>'
        cleaned_html = bleach.clean(
            html_with_allowed_css,
            tags=['p'],
            attributes={'p': ['style']},
            css_sanitizer=css_sanitizer
        )
        print("\nTest 1: HTML with allowed CSS properties")
        print(f"Input:  {html_with_allowed_css}")
        print(f"Output: {cleaned_html}")
        if 'color: blue' in cleaned_html and 'font-size: 16px' in cleaned_html:
            print("✓ Allowed CSS properties were preserved")
        else:
            print("✗ Allowed CSS properties were removed incorrectly")
        
        # Test 3: Sanitize HTML with disallowed CSS
        html_with_disallowed_css = '<p style="color: red; position: absolute; top: 0; left: 0;">This text has disallowed CSS</p>'
        cleaned_html = bleach.clean(
            html_with_disallowed_css,
            tags=['p'],
            attributes={'p': ['style']},
            css_sanitizer=css_sanitizer
        )
        print("\nTest 2: HTML with disallowed CSS properties")
        print(f"Input:  {html_with_disallowed_css}")
        print(f"Output: {cleaned_html}")
        if 'color: red' in cleaned_html and 'position: absolute' not in cleaned_html:
            print("✓ Disallowed CSS properties were correctly removed")
        else:
            print("✗ Disallowed CSS properties were not properly filtered")
        
        print("\n✅ CSS sanitizer is working correctly!")
        return True
        
    except ImportError as e:
        print(f"✗ Failed to import CSS sanitizer: {e}")
        print("\nMake sure you have installed bleach with the CSS sanitizer:")
        print("pip install 'bleach[css]'")
        return False
    except Exception as e:
        print(f"✗ Error during testing: {e}")
        return False

def test_markdown_integration():
    """Test the integration with markdown_filters module from the project"""
    print("\nTesting Integration with Project's Markdown Filters")
    print("=================================================")
    
    try:
        # Import the project's markdown filter
        from cms.templatetags.markdown_filters import markdown_to_html, CSS_SANITIZER_AVAILABLE
        
        print(f"CSS Sanitizer Available: {CSS_SANITIZER_AVAILABLE}")
        
        if CSS_SANITIZER_AVAILABLE:
            print("✓ CSS Sanitizer is available in project's markdown filters")
        else:
            print("✗ CSS Sanitizer is not available in project's markdown filters")
            print("  This may indicate a configuration issue or incompatible version")
            return False
        
        # Test with a markdown sample containing CSS
        markdown_sample = """
# Sample Heading

This is a paragraph with <span style="color: blue; font-size: 18px; position: absolute;">styled text</span>.

<div style="background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;">
  This is a div with styling that should be filtered.
</div>
"""
        html_result = markdown_to_html(markdown_sample)
        print("\nMarkdown to HTML conversion result:")
        print("---------------------------------")
        print(html_result)
        
        # Check if the allowed styles were preserved and disallowed ones removed
        if 'color: blue' in html_result and 'position: absolute' not in html_result:
            print("\n✓ Markdown filter correctly sanitized CSS in HTML output")
            return True
        else:
            print("\n✗ Markdown filter did not properly sanitize CSS")
            return False
        
    except ImportError as e:
        print(f"✗ Failed to import project markdown filters: {e}")
        return False
    except Exception as e:
        print(f"✗ Error during markdown integration testing: {e}")
        return False

if __name__ == "__main__":
    # Run the tests
    sanitizer_test_ok = test_css_sanitizer()
    
    if sanitizer_test_ok:
        project_integration_ok = test_markdown_integration()
        
        if project_integration_ok:
            print("\n✅ All tests passed! Bleach CSS sanitizer is properly configured.")
            sys.exit(0)
        else:
            print("\n⚠️ CSS sanitizer is working but project integration has issues.")
            sys.exit(1)
    else:
        print("\n❌ CSS sanitizer tests failed.")
        sys.exit(1)
