from setuptools import setup, find_packages
from gisea.__version__ import __version__
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    python_requires='>=3.8',
    name='GISEA',
    description="Genetic Interaction Networks and Pathway Modules",
    packages=find_packages(include=['gisea', 'gisea.*']),
    # install_requires=[
    #     "pandas",
    # ],
    version=__version__,
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/x-rst',
)