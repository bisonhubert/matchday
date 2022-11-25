from setuptools import setup

INSTALL_REQUIRES = [
    "pytest==7.2.0"
    # "tools-db>=0.17.0,<1.0.0",
    # "tools-storage>=0.11.0,<1.0.0",
    # "click>=7.1.2,<7.2.0",
    # "tools-secrets>=0.3.7,<1.0.0",
    # "tools-google>=2.0.9,<3.0.0",
    # "tools-cloud-functions>=0.1.2,<1.0.0",
    # "docstring-parser>=0.7.2,<0.8.0",
    # "deprecated>=1.2.10,<1.3.0",
    # "pandas>=0.24.2",
    # "importlib-metadata==4.5.0",
]

setup(
    name="matchday",
    version="0.0.0",
    packages=["matchday"],
    entry_points={"console_scripts": ["matchday = matchday.__main__:main"]},
    install_requires=INSTALL_REQUIRES,
)
