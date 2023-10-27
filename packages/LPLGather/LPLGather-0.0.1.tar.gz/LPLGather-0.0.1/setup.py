
from setuptools import setup, find_packages

setup(
    name="LPLGather",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["polars", "msgspec", "requests"],
    author="Mateus Paulo",
    author_email="maatanalista@gmail.com",
    description="Gather data for LPL players"
)
