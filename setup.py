import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')

setup(
    name = 'django_linksharing',
    version = '0.1',
    url = 'http://github.com/originell/linksharing',
    description = 'Share links with users',
    long_description = README,

    author = 'Luis Nell',
    author_email = 'luis@originell.org',
    packages = [
        'django_linksharing',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers'
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
   ]
)
