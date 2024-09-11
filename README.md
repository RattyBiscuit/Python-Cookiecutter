# Python Cookiecutter

<!-- badges-begin -->

<!-- [![Python Version][python version badge]][github page] -->
[![Status][status badge]][status badge]
[![CalVer][calver badge]][calver]
[![License][license badge]][license]<br>
<!-- [![Read the documentation][readthedocs badge]][readthedocs page] -->
[![Codecov][codecov badge]][codecov page]
[![pre-commit enabled][pre-commit badge]][pre-commit project]
[![Black codestyle][black badge]][black project]
[![Contributor Covenant][contributor covenant badge]][code of conduct]

[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black project]: https://github.com/psf/black
[calver badge]: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
[calver]: http://calver.org/
[code of conduct]: https://github.com/rattybiscuit/python-cookiecutter/blob/main/CODE_OF_CONDUCT.md
[codecov badge]: https://codecov.io/gh/rattybiscuit/python-cookiecutter-instance/branch/main/graph/badge.svg
[codecov page]: https://codecov.io/gh/rattybiscuit/python-cookiecutter-instance
[contributor covenant badge]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
<!-- [github page]: https://github.com/rattybiscuit/python-cookiecutter -->
[license badge]: https://img.shields.io/github/license/rattybiscuit/python-cookiecutter
[license]: https://opensource.org/licenses/MIT
[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit project]: https://pre-commit.com/
<!-- [python version badge]: https://img.shields.io/pypi/pyversions/rattybiscuit-python-cookiecutter-instance -->
<!-- [readthedocs badge]: https://img.shields.io/readthedocs/rattybiscuit-python-cookiecutter/latest.svg?label=Read%20the%20Docs
[readthedocs page]: https://rattybiscuit-python-cookiecutter.readthedocs.io/ -->
[status badge]: https://badgen.net/badge/status/alpha/d8624d

A reduced fork of the [Hypermodern Python Cookiecutter] template by [@cjolowicz].

[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python

## Usage

```console
cookiecutter gh:rattybiscuit/python-cookiecutter
```

## Features

<!-- features-begin -->

- Packaging and dependency management with [Poetry]
- Test automation with [Nox]
- Linting with [pre-commit] and [Flake8]
- Documentation with [Sphinx], [MyST], and [Read the Docs] using the [furo] theme
- Automated uploads to [PyPI] and [TestPyPI]
- Automated dependency updates with [Dependabot]
- Code formatting with [Black] and [Prettier]
- Import sorting with [isort]
- Testing with [pytest]
- Code coverage with [Coverage.py]
- Command-line interface with [Click]
- Automated Python syntax upgrades with [pyupgrade]
- Generate API documentation with [autodoc] and [napoleon]
- Generate command-line reference with [sphinx-click]

The template supports Python 3.7, 3.8, 3.9, and 3.10.

[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[black]: https://github.com/psf/black
[click]: https://click.palletsprojects.com/
[coverage.py]: https://coverage.readthedocs.io/
[dependabot]: https://github.com/dependabot/dependabot-core
[flake8]: http://flake8.pycqa.org
[furo]: https://pradyunsg.me/furo/
[isort]: https://pycqa.github.io/isort/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[pypi]: https://pypi.org/
[pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade
[read the docs]: https://readthedocs.org/
[sphinx]: http://www.sphinx-doc.org/
[sphinx-click]: https://sphinx-click.readthedocs.io/
[testpypi]: https://test.pypi.org/

<!-- features-end -->
