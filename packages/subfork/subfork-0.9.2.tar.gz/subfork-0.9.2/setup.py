#!/usr/bin/env python
#
# Copyright (c) 2022-2023 Subfork. All rights reserved.
#

import os
import sys
import codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
lib = os.path.join(here, "lib")
sys.path.insert(0, lib)


try:
    from subfork import __version__

except ImportError:
    import traceback; traceback.print_exc()
    print("could not import subfork")
    sys.exit(1)


def read(*parts):
    return codecs.open(os.path.join(here, *parts), "r").read()


setup(
    name="subfork",
    description="Subfork Python API",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Subfork",
    author_email="help@subfork.com",
    package_dir={"": "lib"},
    packages=find_packages("lib"),
    version=__version__,
    scripts = ["bin/subfork", "bin/worker"],
    install_requires=[
        "jsmin==3.0.1",
        "psutil==5.9.3",
        "PyYAML==5.3.1",
        "requests==2.25.1",
        "urllib3==1.26.3",
    ],
    zip_safe=False
)
