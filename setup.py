#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Thanks to Kenneth Reitz, I stole the template for this

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

PYTHON3 = sys.version_info[0] > 2

required = []
if not PYTHON3:
    required += ['importlib>=1.0.4']

packages = ['limbo', 'limbo.plugins']

try:
    longdesc = open("README.rst").read()
except:
    longdesc = ''

setup(
    name='slackbot-raspbian',
    version='1.0.0',
    description='Simple Slack Chatbot iRaspbian integration with jenkins, thanks to https://github.com/llimllib/limbo',
    long_description=longdesc,
    author='Rifki Chaplin',
    author_email='rifkichaplin@gmail.com',
    url='https://github.com/llimllib/limbo',
    packages=packages,
    scripts=['bin/limbo'],
    package_data={'': ['LICENSE',], '': ['limbo/plugins/*.py']},
    include_package_data=True,
    install_requires=required,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords="slackbot slack chatbot chat raspbian raspberry",
)
