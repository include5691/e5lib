from setuptools import setup, find_packages

setup(
    name='e5lib',
    version='0.1.0',
    author='Andrey Pshenitsyn',
    description='Bitrix24 rest api automatization utils library',
    packages=find_packages(),
    install_requires=[
        'sqlalchemy',
    ],
)