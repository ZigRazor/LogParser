#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
from setuptools import setup

changelog_url = 'https://github.com/ZigRazor/LogParser/releases'


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='LogParser',
    version='0.0.1',
    license='GNU GENERAL PUBLIC LICENSE',
    description='LogParser Package',
    long_description='%s\n' % (
        re.compile(
            '^.. start-badges.*^.. end-badges',
            re.M | re.S
        ).sub('', read('README.md')),
    ),
    long_description_content_type='text/markdown',
    author='ZigRazor',
    author_email='zigrazor@gmail.com',
    url='https://github.com/ZigRazor/LogParser',
    packages=[],
    package_dir={"" : "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    data_files=[('', ['LICENSE']), ('', ['README.md'])],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries',
    ],
    project_urls={
        'Changelog': changelog_url,
        'Issue Tracker': 'https://github.com/ZigRazor/LogParser/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
        'development',
        'state',
        'log',
        'parser',
        'analysis',
    ],
    python_requires='>=3',
    install_requires=[],
    extras_require={},
    setup_requires=[
        'pytest-runner',
    ],
    entry_points={
        'console_scripts': [
            'nameless = nameless.cli:main',
        ]
    },
)
