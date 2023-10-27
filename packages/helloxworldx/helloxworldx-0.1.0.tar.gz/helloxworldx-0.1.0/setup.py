# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['helloxworldx']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'helloxworldx',
    'version': '0.1.0',
    'description': '',
    'long_description': 'wow this is my projectr\n',
    'author': 'alok',
    'author_email': 'alokmilenium@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
