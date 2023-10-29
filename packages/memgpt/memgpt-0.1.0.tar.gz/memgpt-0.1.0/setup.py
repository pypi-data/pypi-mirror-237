from setuptools import setup, find_packages

setup(
    name="memgpt",
    version="0.1.0",
    author="Norwegian Brain Initiative",
    license="Apache License, Version 2.0",
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
)
