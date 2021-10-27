"""Makes project pip installable"""

from setuptools import find_packages, setup

setup(
    name='chess_game',
    packages=find_packages(),
    version='0.1.0',
    description='Solutions to a series of interview questions',
    author='Logan Rudd',
    license='',
)
