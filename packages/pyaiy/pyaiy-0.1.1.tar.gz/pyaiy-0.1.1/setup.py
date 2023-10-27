from setuptools import setup
from setuptools import find_packages


VERSION = '0.1.1'

setup(
    name='pyaiy',  # package name
    version=VERSION,  # package version
    description='aiy',  # package description
    packages=find_packages(),
    zip_safe=False,
)
