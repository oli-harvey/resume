from setuptools import setup, find_packages

setup(
    name='resume',
    version='0.1.0',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'flask'
    ]
)