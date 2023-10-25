from setuptools import setup, find_packages
from warnings import warn
import sys

# ----------- python version check
if sys.version_info.major != 3 or sys.version_info.minor < 6:
    print(sys.version_info)
    raise SystemError('Module written for Python 3.6+.')

# -------------- fill docstring
import os

this_directory = os.path.abspath(os.path.dirname(__file__))
if os.path.exists(os.path.join(this_directory, 'README.md')):
    # there is no manifest.in file, so it could be missing
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        __doc__ = f.read()

description = f'An official Python3 module to query the cheese chemical space search server (https://cheese.themama.ai/)'

setup(
    name='cheese-python3-api',
    version='1.0.0',
    python_requires='>=3.7',
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/the-mama-ai/cheese-python-api',
    license='MIT',
    author='The MAMA AI',
    author_email='',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description=description,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)