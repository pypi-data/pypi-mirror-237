# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chromadb']

package_data = \
{'': ['*']}

install_requires = \
['opentelemetry-api>=1.19.0,<2.0.0',
 'opentelemetry-instrumentation>=0.40b0,<0.41',
 'opentelemetry-semantic-conventions-ai>=0.0.6,<0.0.7',
 'opentelemetry-semantic-conventions>=0.40b0,<0.41']

setup_kwargs = {
    'name': 'opentelemetry-instrumentation-chromadb',
    'version': '0.0.3',
    'description': 'OpenTelemetry Chroma DB instrumentation',
    'long_description': '# opentelemetry-instrumentation-chromadb\n\nProject description here.\n',
    'author': 'Gal Kleinman',
    'author_email': 'gal@traceloop.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4',
}


setup(**setup_kwargs)
