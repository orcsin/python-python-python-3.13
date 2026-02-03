# Hello World Flask App

A simple hello world Flask app

## Building the Package

To build the distribution package for uploading to Nexus or PyPI:

```bash
# Install build dependencies
pip install -r requirements.txt

# Build the source distribution
python setup.py sdist

# The package will be created in dist/hello_world-1.0.0.tar.gz
```

## Uploading to Nexus

```bash
# Verify the package
twine check dist/hello_world-1.0.0.tar.gz

# Upload to Nexus
twine upload dist/hello_world-1.0.0.tar.gz
```

## Important Notes for Python 3.13

- Make sure to use `setuptools<70` to avoid metadata compatibility issues with twine
- Use `python setup.py sdist` to create the distribution package, NOT `python setup.py build install`