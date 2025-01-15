from setuptools import setup, find_packages

setup(
    name='e5lib',
    version='0.1.0',
    author='Andrey Pshenitsyn',
    description='Utils library',
    packages=find_packages(),
    install_requires=[
        'sqlalchemy',
        'psycopg2-binary',
        'au_b24'
    ],
)