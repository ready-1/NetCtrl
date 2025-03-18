"""
Simple test file that ensures basic functionality works
"""
import pytest

def test_health_check():
    """Simple test that always passes to verify test environment is working"""
    assert True

if __name__ == "__main__":
    pytest.main(["-v", __file__])
