from setuptools import setup, find_packages

VERSION = "0.1.1"
DESCRIPTION = "TagOne Client"

setup(
    name="tagone",
    version=VERSION,
    author="Junior Vidotti",
    author_email="jrvidotti@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests"],
)
