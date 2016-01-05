#Setup file
from setuptools import setup, find_packages
setup(
    name = 'Greengraph',
    version = '0.1',
    description = 'Greengraph - counts green space between two locations'
    packages = find_packages(exclude=['*test']), #Ignore the test-file
    # scripts = ['scripts/Greengraph'], # Note sure yet if needed
    install_requires = ['argparse', 'geopy']
)
