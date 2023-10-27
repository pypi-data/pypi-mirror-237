from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'beauty of vandna'
LONG_DESCRIPTION = 'A package to describe beauty of vandna'

# Setting up
setup(
    name="vandu",
    version=VERSION,
    author="jam.code",
    author_email="jamunaprasadyaadavrnq@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['vandu', 'math', 'mathematics', 'jam.code', 'vandna'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)