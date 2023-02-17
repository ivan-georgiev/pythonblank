"""
Default
"""
import main


def test_dummy():
    """
    Default
    """
    assert main.dummy(inp='testme') == 'testme'


def test_dummy1():
    """
    Default
    """
    assert main.dummy1(inp='testme') == 'dummy1:testme'


def test_dummy1_2(mocker):
    """
    Default
    """
    mocker.patch('main.dummy', return_value='static')
    assert main.dummy1(inp='testme') == 'dummy1:static'

# tested uses imported module


def test_dummy2():
    """
    Default
    """
    assert main.dummy2() == 'd2:mod:echo from main'


def test_dummy2_1(mocker):
    """
    Default
    """
    mocker.patch('main.mod.moddummy', return_value='static')
    assert main.dummy2() == 'd2:static'

# using fixtures


def test_1(input_value):
    """
    Default
    """
    assert main.dummy(inp=input_value) == 'fixme'


def test_2(read_input):
    """
    Default
    """
    assert main.dummy(inp=read_input) == '{"key": "value"}'
