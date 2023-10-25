from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pycryptomod',
    version='0.1.0',
    description='A simpler plug and play module for prototyping cryptography techniques',
    long_description=long_description,
    long_description_content_type='text/markdown', 
    author='Aditya Bharadwaj',
    author_email='adityabharadwaj47@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pycryptodome',  # Include the required packages
    ],
    license='MIT',  # Specify the license
)
