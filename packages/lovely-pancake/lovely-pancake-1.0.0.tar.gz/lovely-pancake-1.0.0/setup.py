from setuptools import setup, find_packages

setup(
    name='lovely-pancake',
    version='1.0.0',
    description='My Python package',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'numpy',
    ],
)