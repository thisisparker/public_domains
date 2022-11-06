#!/bin/bash

# release to pypi!

rm -rf dist
python3 setup.py sdist bdist_wheel
twine upload dist/*

