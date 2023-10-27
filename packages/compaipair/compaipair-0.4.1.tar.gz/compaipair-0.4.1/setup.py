# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['compaipair',
 'compaipair.complete',
 'compaipair.config',
 'compaipair.templates',
 'compaipair.types']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.7,<9.0.0',
 'google-generativeai>=0.2.2,<0.3.0',
 'pydantic>=2.4.2,<3.0.0',
 'pytest>=7.4.2,<8.0.0',
 'python-dotenv>=1.0.0,<2.0.0',
 'rich>=13.6.0,<14.0.0',
 'tinydb>=4.8.0,<5.0.0']

entry_points = \
{'console_scripts': ['compai = compaipair.main:compai']}

setup_kwargs = {
    'name': 'compaipair',
    'version': '0.4.1',
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
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
