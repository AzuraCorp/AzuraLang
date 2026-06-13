from setuptools import setup, find_packages

setup(
    name='AzuraLang',
    version='BETA-1',
    author='Zhan2os1ks',
    description='A lightweight, native GUI framework for Python',
    # Automatically finds the AzuraLang folder with your __init__.py
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # Standard dependencies your framework needs to run
    install_requires=[
        'colorama',
    ],
)