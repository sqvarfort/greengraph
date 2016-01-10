#Setup file
from setuptools import setup, find_packages
setup(
    name = 'Greengraph',
    version = '0.1',
    description = 'Greengraph - counts green space between two locations',
    packages = find_packages(exclude=['*test']),
    install_requires = ['argparse', 'geopy']
)
