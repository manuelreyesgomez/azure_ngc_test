#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

setup(
    name="azureml_ngc_test",
    version='0.1.8',
    description="AzureML integration with NGC",
    url="",
    keywords="azureml,ngc,gpu",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    long_description=(open("README.md").read() if exists("README.md") else ""),
    zip_safe=False,
    install_requires=[
       "aiobotocore>=1.0.7",
       "dask>=2.2.0",
       "distributed>=2.3.1",
       "azureml-sdk>=1.0.83"
   ],
    entry_points="""
    """,
    python_requires=">=3.5",
)
