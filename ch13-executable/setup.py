#!/usr/bin/env python

"""The setup script."""

from setuptools import setup

requirements = [
    "requests>=2.25",
]

setup(
    author="Sebastian Witowski",
    author_email="sebastian@switowski.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="GUI tool to ping websites and return their HTTP codes.",
    entry_points={
        "console_scripts": [
            "guptimer=guptimer.gui:main",
            ]
    },
    install_requires=requirements,
    license="MIT license",
    keywords="guptimer",
    name="guptimer",
    packages=["guptimer"],
    url="https://github.com/switowski/guptimer",
    version="0.1.0",
    zip_safe=False,
)
