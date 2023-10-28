from setuptools import setup, find_packages

setup(
    name='2023_assignment1_DevOps',
    version='1.0.0',
    description='Assignment1',
    author='Luca Perfetti',
    author_email='l.perfetti2001@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pymongo',
        'pytest', 
        'prospector',
        'bandit',
        'mkdocs',
    ],
)
