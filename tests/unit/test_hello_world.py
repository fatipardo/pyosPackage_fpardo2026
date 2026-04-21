"""
A test module that tests the hello_world.py module
"""

from pyospackage_fpardo2026.hello_world import hello_world

def test_hello_world():
    """
    Test that hello_world works as expected.

    """
    out = hello_world("spanish")
    expected_out = 'hola mundo'
    assert  out == expected_out, f"Expected {expected_out} but got {out}"