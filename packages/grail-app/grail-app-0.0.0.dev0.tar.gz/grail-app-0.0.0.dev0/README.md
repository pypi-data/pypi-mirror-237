
<!--[[[cog import gen; cog.out(gen.readme()) ]]]-->

# This is the readme for this project

<!--[[[end]]]-->


## Publishing

### 1. Build the package

`python -m build`

`twine check dist/*`

### 2. Upload to PyPI

`twine upload dist/* --verbose`