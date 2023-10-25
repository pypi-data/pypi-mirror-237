# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hrtx']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'torch']

setup_kwargs = {
    'name': 'hrtx',
    'version': '0.0.1',
    'description': 'HRTX - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# HRTX\nHivemind Multi-Modality Transformer (HMMT) Model Architecture \n\n\nMulti-Modality Model that can ingest text and video modalities from an x amount of models at the same time and then output instructions for each robot or any N number of robots\n\n\n# License\nMIT\n\n\n\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/hrtx',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
