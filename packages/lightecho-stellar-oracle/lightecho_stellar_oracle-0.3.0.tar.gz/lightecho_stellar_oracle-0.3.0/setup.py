# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['lightecho_stellar_oracle']
install_requires = \
['stellar-sdk==9.0.0b0']

setup_kwargs = {
    'name': 'lightecho-stellar-oracle',
    'version': '0.3.0',
    'description': 'Python SDK for the Lightecho Stellar Oracle',
    'long_description': '**Python SDK for the Lightecho Stellar Oracle**\n\nFor more information see [https://github.com/bp-ventures/lightecho-stellar-oracle](https://github.com/bp-ventures/lightecho-stellar-oracle).\n',
    'author': 'BP Ventures',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bp-ventures/lightecho-stellar-oracle/tree/trunk/oracle-sdk/python',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
