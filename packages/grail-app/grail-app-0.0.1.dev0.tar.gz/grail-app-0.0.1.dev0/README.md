
<!--[[[cog import gen; cog.out(gen.readme()) ]]]-->

# This is the readme for this project

<!--[[[end]]]-->


## Publishing

### 0. Increment the version

Edit `__version__` in `__init__.py`

### 1. Build the package

`python -m build`

`twine check dist/*`

### 2. Upload to PyPI

`twine upload dist/* --verbose`