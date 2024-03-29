#!/usr/bin/env python3
from setuptools import setup

setup(
    name="tap-hudsonltd",
    version="0.1.1",
    description="Singer.io tap for extracting data",
    author="Simon Data",
    url="http://simondata.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_hudsonltd"],
    install_requires=[
        "singer-python==5.2.0",
        "requests==2.18.4",
        "xmltodict==0.11.0",
        "bs4==0.0.1",
        "tap-kit @ git+https://github.com/Radico/tap-kit.git@main"
    ],
    dependency_links=[
        "https://github.com/Radico/tap-kit/tarball/main#egg=tap-kit-0.1.1",
    ],
    entry_points="""
    [console_scripts]
    tap-hudsonltd=tap_hudsonltd:main
    """,
    packages=["tap_hudsonltd"],
    include_package_data=True,
)
