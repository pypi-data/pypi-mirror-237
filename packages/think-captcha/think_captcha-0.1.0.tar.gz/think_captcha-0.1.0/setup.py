from setuptools import setup, find_packages

setup(
    name="think_captcha",
    version="0.1.0",
    description="A simple Python package for solving captcha",
    author='Ibrohim Fayzullayev',
    author_email='ibrohimfayzullayev79@gmail.com',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)