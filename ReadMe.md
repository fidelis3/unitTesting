# Unit Testing Practice Project

This repository is a simple Python project for practicing unit testing with the built-in `unittest` framework.

## Overview

The project includes:

- Basic math/helper functions in `mymodule.py` and `mymodule2.py`
- Test files using `unittest` in `test_mymodule.py` and `test_mymodule2.py`

## Functions

### `mymodule.py`

- `square(number)`: returns the square of `number`
- `double(number)`: returns twice the value of `number`

### `mymodule2.py`

- `add(a, b)`: returns the sum of `a` and `b`

## Project Structure

```text
.
|- mymodule.py
|- mymodule2.py
|- test_mymodule.py
|- test_mymodule2.py
|- ReadMe.md
```

## Requirements

- Python 3.x
- No external packages are required

## How To Run Tests

From the project root, you can run all tests:

```bash
python -m unittest
```

Run a specific test file:

```bash
python -m unittest test_mymodule.py
python -m unittest test_mymodule2.py
```

Run a test file directly:

```bash
python test_mymodule.py
python test_mymodule2.py
```


