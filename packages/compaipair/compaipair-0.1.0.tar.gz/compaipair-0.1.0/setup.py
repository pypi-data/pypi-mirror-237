# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['compaipair']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.7,<9.0.0', 'google-generativeai>=0.2.2,<0.3.0']

setup_kwargs = {
    'name': 'compaipair',
    'version': '0.1.0',
    'description': 'A simple CLI for pair programming with Google Generative AI APIs',
    'long_description': None,
    'author': 'Andrés Arango Pérez',
    'author_email': 'andresap@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
