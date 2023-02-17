"""
Default
"""
import os
import pytest


@pytest.fixture
def input_value():
    """
    Default
    """
    yield 'fixme'


@pytest.fixture
def read_input():
    """
    Default
    """
    with open(file=os.path.join('tests', 'data', 'input1.json'), mode='r') as f:
        yield f.read()
