"""
A test module that tests the repeat_text.py module
"""

from pyospackage_fpardo2026.repeat_text import repeat_text

def test_repeat_text():
    """
    Test that repeat_text works as expected.

    """
    out = repeat_text("cat", 3)
    expected_out = "catcatcat"
    assert  out == expected_out, f"Expected {expected_out} but got {out}"