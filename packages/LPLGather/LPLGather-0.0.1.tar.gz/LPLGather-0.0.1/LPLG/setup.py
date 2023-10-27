
from setuptools import setup, find_packages

setup(
    name='LPLG',
    version='0.0.1',
    packages=find_packages(),
    author='Mateus Paulo',
    author_email='maatanalista@gmail.com',
    description='Gather data for LPL players',
    install_requires=[
        'polars',
        'msgspec',
        'requests'
    ]
)
