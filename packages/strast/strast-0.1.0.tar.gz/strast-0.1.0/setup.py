# Copyright (c) 2023 Jan T. Müller <mail@jantmueller.com>

import sys
import os
from setuptools import setup, find_packages
import strast


if sys.version_info < (3, 6):
    sys.exit("ERROR: strast requires Python 3.6+")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="strast",
    version=strast.__version__,
    packages=find_packages(exclude=["tests"]),
    author="Jan T. Müller",
    author_email="mail@jantmueller.com",
    description="Transforms a string representation of a Python literal into the corresponding Python object.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/janthmueller/strast",
    project_urls={
        "Documentation": "https://janthmueller.github.io/strast/docs/strast.html",
        "Source": "https://github.com/janthmueller/strast",
        "Tracker": "https://github.com/janthmueller/strast/issues",
    },
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.6",
)
