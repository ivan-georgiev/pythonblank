"""
Just an example
"""
from module1 import mod


def dummy(inp: str) -> str:
    """
    Default
    """
    return inp


def dummy1(inp: str) -> str:
    """
    Default
    """
    return 'dummy1:' + dummy(inp=inp)


def dummy2() -> str:
    """
    Default
    """
    v = mod.moddummy(inp='echo from main')
    return f'd2:{v}'


def main():
    """
    Default
    """
    print(dummy2())


if __name__ == '__main__':
    main()
