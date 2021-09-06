from setuptools import setup, find_packages
# To use a consistent encoding; see https://docs.python.org/2/library/codecs.html
from codecs import open
from os import path
import re

from account_api import __version__ as version
from account_api import __author__ as author_info
from account_api import __license__ as license

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


name = 'account_api'
description = 'Alembic -> REST Api Utility'
url = 'https://github.com/phonybone/'+name
mg = re.match(r'(.*) <([^>]+)>', author_info)
author = mg.group(1)
author_email = mg.group(2)

classifiers = [          # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    # 'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    # 'Intended Audience :: Developers',
    # 'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
    # 'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    # 'Programming Language :: Python :: 2',
    # 'Programming Language :: Python :: 2.6',
    # 'Programming Language :: Python :: 2.7',
    # 'Programming Language :: Python :: 3',
    # 'Programming Language :: Python :: 3.3',
    # 'Programming Language :: Python :: 3.4',
    # 'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
],
keywords = ''
packages = find_packages(exclude=[])
install_requires = []
extras_require = {
    'dev': [],
    'test': ['pytest'],
}
package_data = {
}
data_files = []
entry_points = {}

setup(
    name=name,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description=description,
    long_description=long_description,

    # The project's main homepage.
    url=url,

    # Author details
    author=author,
    author_email=author_email,

    # Choose your license
    license=license,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=classifiers,

    # What does your project relate to?
    keywords=keywords,

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=packages,

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=install_requires,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require=extras_require,

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data=package_data,

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=data_files,

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points=entry_points,
)

