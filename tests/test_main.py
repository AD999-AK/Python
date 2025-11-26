"""Tests for the main module."""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from main import hello_world


def test_hello_world() -> None:
    """Test the hello_world function."""
    assert hello_world() == "Hello, World!"
