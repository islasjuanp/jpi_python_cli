from setuptools import setup, find_packages

setup(
    name='python_cli',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'python_cli = src.main:main',
        ],
    },
)