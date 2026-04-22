"""
A test module that tests the hello_world.py module
"""

import pytest
from pyospackage_fpardo2026.hello_world import hello_world


@pytest.mark.parametrize(
    "language, expected_out",
    [
        ("spanish", "hola mundo"),
        ("english", "hello world"),
        ("portuguese", "oi mundo"),
    ],
)
def test_hello_world_valid_languages(language, expected_out):
    assert hello_world(language) == expected_out


@pytest.mark.parametrize(
    "language, expected_out",
    [
        (" Spanish ", "hola mundo"),
        ("ENGLISH", "hello world"),
        (" portuguese ", "oi mundo"),
    ],
)
def test_hello_world_normalized_input(language, expected_out):
    assert hello_world(language) == expected_out


def test_hello_world_unsupported_language():
    with pytest.raises(ValueError, match="Unsupported language"):
        hello_world("french")


def test_hello_world_non_string():
    with pytest.raises(TypeError, match="language must be a string"):
        hello_world(123)