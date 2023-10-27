from setuptools import setup

name = "types-cachetools"
description = "Typing stubs for cachetools"
long_description = '''
## Typing stubs for cachetools

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`cachetools`](https://github.com/tkem/cachetools) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`cachetools`.

This version of `types-cachetools` aims to provide accurate annotations
for `cachetools==5.3.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/cachetools. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `1c184fea33d50ba430410cf1b25d4aea2df2981e` and was tested
with mypy 1.6.1, pyright 1.1.332, and
pytype 2023.10.17.
'''.lstrip()

setup(name=name,
      version="5.3.0.7",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/cachetools.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['cachetools-stubs'],
      package_data={'cachetools-stubs': ['__init__.pyi', 'func.pyi', 'keys.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      python_requires=">=3.7",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
