from setuptools import setup, find_packages

setup(
    name='producthunt',
    version='0.0.1',
    url='https://github.com/dariubs/producthunt.py',
    author='Dariush Abbasi',
    author_email='poshtehani@gmail.com',
    description='Producthunt API wrapper for python',
    packages=find_packages(),    
    install_requires=['requests', 'graphene'], 
)
