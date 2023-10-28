from setuptools import setup, find_packages

setup(
    name="farans-test-package",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample Python package for testing PyPI",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/faranpde/PyPI-test",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)