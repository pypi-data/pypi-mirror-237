# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lib2to3']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mff-lib2to3-fake',
    'version': '0.1.0',
    'description': 'Stub copying part of the lib2to3 API to allow Py-Feat to work with Python 3.10+ (no functionality).',
    'long_description': '# Lib2to3 Fake\n\nThis package provides a partial imitation of the `lib2to3` API (without any functionality). This is done in order to allow Py-Feat 0.6.1 to work in Python 3.10+.\n',
    'author': 'Marc Fraile',
    'author_email': 'marc.fraile.fabrega@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
