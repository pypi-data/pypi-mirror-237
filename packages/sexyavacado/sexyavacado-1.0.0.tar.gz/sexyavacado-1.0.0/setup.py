from setuptools import setup, find_packages

setup(
    name='sexyavacado',
    version='1.0.0',
    description='My lovely python package',
    author='Duzduran',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'numpy',
    ],
)