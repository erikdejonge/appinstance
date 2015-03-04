#!/usr/bin/env bash
git commit -am "-"
rm -Rf build
rm -Rf dist

python setup.py register
python setup.py build
python setup.py sdist
python setup.py sdist upload
