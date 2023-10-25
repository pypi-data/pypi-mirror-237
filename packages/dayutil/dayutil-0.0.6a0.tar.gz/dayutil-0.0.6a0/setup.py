# -*- coding:utf-8 -*-


import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dayutil",
    version="0.0.6a",
    author="haitanghuadeng",
    author_email="491609917@qq.com",
    description="See Day.js for Python's time-handling library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/haitanghuadeng/dayutil",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
