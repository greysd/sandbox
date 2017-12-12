#!/usr/bin/env python
# encoding: utf-8
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Dirty hack to prevent ``python setup.py sdist`` from making hard links:
# it doesn't work in VMWare/VBox shared folders.
import os
del os.link


setup(
    name='apiserver',
    version='1.0',
    license='BSD',
    description='TCPIP Admin Sandbox',
    long_description=__doc__,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    packages=['apiserver'],
    include_package_data=True,
    zip_safe=False,
    platforms='any'
)
