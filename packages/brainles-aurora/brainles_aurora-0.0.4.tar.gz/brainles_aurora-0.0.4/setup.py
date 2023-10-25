# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['brainles_aurora']

package_data = \
{'': ['*']}

install_requires = \
['PyGithub>=1.57',
 'monai>=1.2.0',
 'nibabel>=4.0.2',
 'numpy>=1.23.0',
 'path>=16.2.0',
 'torch>=2.1.0',
 'tqdm>=4.64.1']

setup_kwargs = {
    'name': 'brainles-aurora',
    'version': '0.0.4',
    'description': 'TODO.',
    'long_description': None,
    'author': 'Florian Kofler',
    'author_email': 'florian.kofler@tum.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
