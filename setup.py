from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import io
import codecs
import os
import sys

import flask_nicely

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

long_description = 'Placeholder'

setup(
    name='Flask-Nicely',
    version=flask_nicely.__version__,
    url='http://github.com/jwpe/flask-nicely/',
    license='BSD',
    author='Jonathan Evans',
    author_email='jwpevans@gmail.com',
    description='Pretty JSON responses for API building.',
    long_description=long_description,
    packages=['flask_nicely'],
    install_requires = ['Flask'],
    include_package_data=True,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    tests_require=['pytest', 'Flask-Testing'],
    test_suite='test',
    cmdclass = {'test': PyTest},
)
