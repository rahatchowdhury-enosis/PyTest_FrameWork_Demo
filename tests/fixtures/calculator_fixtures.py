import pytest
from src.calculator import Calculator


@pytest.fixture
def calc():
    """Returns a Calculator instance."""
    return Calculator()
