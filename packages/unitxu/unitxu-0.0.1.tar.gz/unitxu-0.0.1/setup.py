#!/usr/bin/env python
# -*- coding=utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="unitxu",
  version="0.0.1",
  author="xjm",
  author_email="2289359795@qq.com",
  description="A small example package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/pypa/sampleproject",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)