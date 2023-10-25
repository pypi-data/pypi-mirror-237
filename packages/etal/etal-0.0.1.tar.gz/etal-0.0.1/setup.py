#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup

setup(
    name="etal",
    version="0.0.1",
    description="Shorten bibliographies.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Benjamin D. Killeen",
    author_email="killeen@jhu.edu",
    url="https://github.com/benjamindkilleen/etal",
    install_requires=["click", "rich", "bibtexparser"],
    packages=find_packages(),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "etal = etal.cli:main",
        ]
    },
)
