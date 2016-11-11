#!/usr/bin/env python
import os
import re

from setuptools import find_packages, setup

here = os.path.dirname(os.path.abspath(__file__))
version_re = re.compile(r'__version__ = (\(.*?\))')
fp = open(os.path.join(here, 'coffin', '__init__.py'))
version = None
for line in fp:
    match = version_re.search(line)
    if match:
        version = eval(match.group(1))
        break
else:
    raise Exception('Cannot find version in __init__.py')
fp.close()

setup(
    name='Coffin',
    version='.'.join(map(str, version)),
    description='Jinja2 adapter for Django',
    author='Christopher D. Leary',
    author_email='cdleary@gmail.com',
    maintainer='Michael Elsdoerfer',
    maintainer_email='michael@elsdoerfer.com',
    url='http://github.com/coffin/coffin',
    packages=find_packages(exclude=('tests',)),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
