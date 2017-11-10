# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

setup(
    name="mansnotbot",
    version="0.0.1",
    author="Benjamin Maisonnas",
    author_email="ben@wainei.net",
    description="Detect botters by username, using machine learning",
    long_description=readme,
    license="GPLv3",
    keywords="bot",
    url="https://github.com/benzhaomin/mansnotbot",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],

    packages=find_packages(exclude=("tests", "docs")),
    package_data={
        "mansnotbot": [],
    },
    test_suite="tests",
    entry_points={
        "console_scripts": ["mansnotbot = mansnotbot.cli:main"],
    },
    install_requires=[],
    extras_require={
        "dev": [
            "flake8",
            "nose",
        ],
    },
)
