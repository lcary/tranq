from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.1.0'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tranq',
    version=__version__,
    description='Toy language built with Python',
    long_description=long_description,
    url='https://github.com/lcary/tranq',
    download_url='https://github.com/lcary/tranq/archive/' +
    __version__,
    license='Apache',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    python_requires='>=3.5',
    author='Luc Cary',
    author_email='luc.cary@gmail.com')
