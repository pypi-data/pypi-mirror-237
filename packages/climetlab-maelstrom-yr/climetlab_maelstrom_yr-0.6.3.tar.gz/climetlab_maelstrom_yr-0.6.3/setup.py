#!/usr/bin/env python


import io
import os

import setuptools


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding="utf-8").read()


package_name = "climetlab_maelstrom_yr"

version = None
init_py = os.path.join(package_name.replace("-", "_"), "__init__.py")
for line in read(init_py).split("\n"):
    if line.startswith("__version__"):
        version = line.split("=")[-1].strip()[1:-1]
assert version

setuptools.setup(
    name=package_name,
    version=version,
    description="A dataset plugin for climetlab for the dataset maelstrom-yr/yr.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Thomas Nipen",
    author_email="thomasn@met.no",
    url="https://github.com/metno/climetlab-maelstrom-yr",
    license="Apache License Version 2.0",
    packages=setuptools.find_packages(),
    install_requires=[
        "argparse",
        "datetime",
        "climetlab>=0.9.0",
        "future",
        "numpy",
        "six",
    ],
    extras_require={
        "test": ["coverage", "pep8"],
    },
    include_package_data=True,
    zip_safe=True,
    entry_points={
        "climetlab.datasets": [
            "maelstrom-yr = climetlab_maelstrom_yr.yr:Yr",
        ],
        "console_scripts": [
            "maelstrom-train=maelstrom:main",
        ],
    },
    keywords="meteorology",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
