from setuptools import setup, find_packages

setup(
    name='ORTipy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib>=3.1',
        'pulp',
    ],
    author='twofoldtwins',
    author_email='twofoldtwinsinc@gmail.com',
    description='Operation Research Toolkit in Python',
    url='https://github.com/cryptbird/OPTipy',
    license='Apache License 2.0',
)
