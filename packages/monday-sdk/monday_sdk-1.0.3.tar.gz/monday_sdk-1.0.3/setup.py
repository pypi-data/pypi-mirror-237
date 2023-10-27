# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['monday_sdk']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.6,<4.0.0',
 'fastapi>=0.88.0,<0.89.0',
 'flask>=2.3.2,<3.0.0',
 'gql>=3.4.1,<4.0.0',
 'numpy>=1.26.1,<2.0.0',
 'pandas>=2.1.1,<3.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'uvicorn>=0.22.0,<0.23.0']

setup_kwargs = {
    'name': 'monday-sdk',
    'version': '1.0.3',
    'description': '',
    'long_description': '# Python SDK for monday.com\n',
    'author': 'Jonathan Crum',
    'author_email': 'jcrum@theobogroup.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/krummja/MondaySDK.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<3.13',
}


setup(**setup_kwargs)
