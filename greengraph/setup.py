#Setup file
from setuptools import setup, find_packages
setup(
    name = 'Greengraph',
    version = '0.1',
    packages = find_packages(excplude=['*test']), #Ignore the test-file
    # scripts = ['scripts/Greengraph'], # Note sure yet if needed
    install_requires = ['argparse']
)
