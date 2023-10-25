## Overview

This project contains a collection of functions for performing various data transformation and analysis tasks, 
including matrix transposition, window generation from 1D arrays, and 2D convolution operations.

Project is published in PyPi: https://pypi.org/project/mjurav-de2-1/.

### Project Structure

```bash
src/
    data_transformation/
        __init__.py
        transform.py
test/
    test_functions.py
poetry.lock
pyproject.toml
README.md
```

### Installation

### Install Poetry

Poetry is a Python dependency management tool.

1. Install Poetry:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
2. Add Poetry to your system's PATH, following the post-installation instructions provided.

---

After installing these prerequisites, proceed with the main project setup as described in the README.

### Install project from GitHub

To download and install project, run commands:

```bash
git clone git@github.com:TuringCollegeSubmissions/mjurav-DE2.1.git
cd mjurav-DE2.1
poetry install
```

### Install as a package from PyPi

Navigate to your project where you want to have `mjurav-DE2.1` package as a dependency, and use poetry add command:

```bash
poetry add mjurav-de2-1
```

### Usage

#### Transposing a 2D Matrix

To transpose a 2D matrix, use the transpose2d function from src/data_transformation/transform.py.

```python
from data_transformation.transform import transpose2d

matrix = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
transposed_matrix = transpose2d(matrix)
print(transposed_matrix)
```

#### Generating Windows from a 1D Array

To generate windows from a 1D array, use the window1d function from src/data_transformation/transform.py.

```python
from data_transformation.transform import window1d

array = [1, 2, 3, 4, 5]
windows = window1d(array, size=2, shift=1, stride=1)
print(windows)
```

#### Applying 2D Convolution

To apply a 2D convolution operation, use the convolution2d function from src/data_transformation/transform.py.

```python
import numpy as np
from data_transformation.transform import convolution2d

input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
kernel = np.array([[1, 0], [0, -1]])
convolved_matrix = convolution2d(input_matrix, kernel)
print(convolved_matrix)
```

### Running Tests

To run the tests, use the following command:

```bash
poetry run python -m unittest tests/test_functions.py
```
