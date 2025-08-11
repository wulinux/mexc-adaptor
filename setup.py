"""Python setup.py for mexc_adaptor package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("mexc_adaptor", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="mexc_adaptor",
    version=read("mexc_adaptor", "VERSION"),
    description="Awesome mexc_adaptor created by wulinux",
    url="https://github.com/wulinux/mexc-adaptor/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="wulinux",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["mexc_adaptor = mexc_adaptor.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
