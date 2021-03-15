import pytest
from .main import add

def test_sample():
    assert add(1,1) == 2
