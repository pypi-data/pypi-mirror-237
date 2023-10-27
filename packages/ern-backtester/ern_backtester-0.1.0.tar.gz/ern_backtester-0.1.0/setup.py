# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

version = {}
with open("ern_backtester/version.py") as file:
    exec(file.read(), version)

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='ern_backtester',
    version=version['__version__'],
    author='Ernest Yuen',
    author_email='ernestyuen08@gmail.com',
    description='Ernest Backtest Framework Library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.9',
    py_modules=["ern_backtester"],
    package_dir={'':'ern_backtester'},
    zip_safe=False,
    install_requires=[
        'vectorbt',
        'pandas',
        'numba',
        'numpy',
        'Bottleneck',
        'matplotlib',
        'pyarrow',
        'statsmodels',
        'seaborn',
    ]
)
