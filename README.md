# wpycounts

Count the number of words in a text file!
1. Documentation: https://wpycounts.readthedocs.io/en/latest/index.html
2. Test PyPI: https://test.pypi.org/project/wpycounts/

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ wpycounts
```

## Usage

`wpycounts` can be used to count words in a text file and plot results
as follows:

```python
from pycounts.pycounts import count_words
from pycounts.plotting import plot_words
import matplotlib.pyplot as plt

file_path = "test.txt"  # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`wpycounts` was created by Wesllen Sousa. It is licensed under the terms of the MIT license.

## Credits

`wpycounts` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
