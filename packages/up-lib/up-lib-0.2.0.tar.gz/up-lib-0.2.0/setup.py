# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['up_lib']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'up-lib',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Julio Faerman',
    'author_email': '356476+faermanj@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.12,<4.0',
}


setup(**setup_kwargs)
