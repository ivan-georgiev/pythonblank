"""
Make a package installable
"""

import os
from setuptools import setup, find_packages
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext


def main():
    """
    Prepare package metadata and install package
    """

    with open(os.path.join('docs', 'README.md'), 'r') as readme_file:
        long_description = readme_file.read()

    requirements = [
        'requests'
    ]

    development = [
        'pytest',
        'pytest-mock',
        'pytest-cov',
        'autopep8',
        'mypy',
        'pylint',
        'pylint-quotes'
    ]

    pkg_setup = {
        'name': 'my_package',
        'version': '0.1.0',
        'description': 'my_package',
        'long_description': long_description,
        'long_description_content_type': 'text/markdown',
        'author': 'Ivan',
        'packages': find_packages('src'),
        'python_requires': '>=3.10',
        'install_requires': requirements,
        'extras_require': {
            'dev': development
        },
        'include_package_data': True,
        'license': 'MIT',
        'classifiers': [
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.10",
            "Operating System :: OS Independent",
        ],
        'package_dir': {'': 'src'},
        'py_modules': [splitext(basename(path))[0] for path in glob('src/*.py')],
    }
    # Do the actual install
    setup(**pkg_setup)


if __name__ == '__main__':
    main()
