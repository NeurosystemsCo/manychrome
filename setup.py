# -*- coding: utf-8 -*-

# Learn more: https://github.com/NeurosystemsCo/manychrome/setup.py

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="manychrome",
    version="0.0.1",
    author="Maria Wenner",
    author_email="mail@neurosystems.co",
    description="A simple package to colour and style your text printed on the CLI.",
    long_description=readme,
    packages=find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: MacOS"
    ],
    python_requires='>=3.8',
    homepage = "https://github.com/NeurosystemsCo/manychrome",
    issues = "https://github.com/NeurosystemsCo/manychrome/issues"
)
