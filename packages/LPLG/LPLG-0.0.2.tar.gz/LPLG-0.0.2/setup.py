
from setuptools import setup, find_packages

setup(
    name="LPLG",
    version="0.0.2",
    packages=find_packages(),
    author="Mateus Paulo",
    author_email="maatanalista@gmail.com",
    description="Gather date for LPL players",
    install_requires=[
        "polars",
        "msgspec",
        "requests",
        "python-dotenv"
    ],
    python_requires='>=3.6',
)

