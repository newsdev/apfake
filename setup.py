import os.path
from pip.download import PipSession
from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename), 'r').read()

setup(
    name='apfake',
    version='0.0.1',
    author='Jeremy Bowers',
    author_email='jeremy.bowers@nytimes.com',
    url='https://github.com/newsdev/apfake',
    description='Command-line interface for extrapolating test data from a single AP API JSON file.',
    long_description=read('README.rst'),
    packages=['apfake'],
    entry_points={
        'console_scripts': (
            'apfake = apfake:main',
        ),
    },
    license="Apache License 2.0",
    keywords='election race candidate democracy news associated press',
    install_requires=['ujson==1.35'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ]
)
