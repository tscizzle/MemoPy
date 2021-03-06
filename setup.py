# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='memopy',
    version='0.0.1',
    description='Memoize / cache function call results',
    long_description=long_description,
    url='https://github.com/tscizzle/memopy',
    author='Tyler Singer-Clark',
    author_email='tscizzle@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
    ],
    keywords='cache memoization function',
    packages=find_packages(),
    install_requires=[],
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
)
