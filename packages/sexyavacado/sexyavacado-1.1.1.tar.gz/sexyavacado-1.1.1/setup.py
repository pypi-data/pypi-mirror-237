from setuptools import setup, find_packages

setup(
    name='sexyavacado',
    version='1.1.1',
    description='My lovely python package',
    author='Duzduran',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'numpy',
    ],
)