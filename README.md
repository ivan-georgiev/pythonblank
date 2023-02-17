
# Python project

## Commands

```PowerShell
# venv
python -m venv venv
. .\venv\Scripts\Activate.ps1

# install dev + prod dependencies
pip install -e .[dev]

# install prod dependencies
pip install -e .

# run tests
pytest
pytest --cov-report term
pytest --cov-report term-missing --cov=module1
pytest --cov-report term-missing --cov=main

# run code
 python src\main.py
```
