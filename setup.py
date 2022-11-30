# Run this setup file with ./install.sh from the root directory

from setuptools import setup

INSTALL_REQUIRES = ["pytest==7.2.0"]

setup(
    name="matchday",
    version="0.0.0",
    packages=["matchday"],
    entry_points={"console_scripts": ["matchday = matchday.__main__:main"]},
    install_requires=INSTALL_REQUIRES,
)
