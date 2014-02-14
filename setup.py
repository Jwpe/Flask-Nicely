from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import io
import codecs
import os
import sys

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

long_description = """
Flask-Nicely consists of a simple decorator with which to wrap Flask
functions that return data in order to turn them into pretty, consistent
JSON responses. It also provides several built in HTTP exceptions which can
be raised in a Flask function in order to return the corresponding HTTP
error response.

Docs can be found at http://flask-nicely.readthedocs.org/
"""

setup(
    name='Flask-Nicely',
    version='0.1.2',
    url='http://github.com/jwpe/flask-nicely/',
    license='BSD',
    author='Jonathan Evans',
    author_email='jwpevans@gmail.com',
    description='Pretty Flask JSON responses for API building.',
    long_description=long_description,
    install_requires = ['Flask'],
    packages=['flask_nicely'],
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
