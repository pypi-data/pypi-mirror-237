# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timeless_loop']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'timeless-loop',
    'version': '0.2.0',
    'description': '',
    'long_description': '# timeless_loop\n\ntimeless_loop is a Python library that provides a custom asyncio event loop, allowing you to freeze time and avoid pesky delays while writing or testing async code.\nIt does so by defining a subclass of the standard library `SelectorEventLoop`, which behaves nearly identically to the real one.\nIt differs in that it does not actually wait for any time to pass; instead, it simply advances the loop\'s internal clock to the exact time of execution of the next scheduled callback when there are no immediately ready loop callbacks available.\nThis allows you to run code that uses asyncio\'s `sleep` and `wait` functions without having to wait for the actual time to pass, without having to change any lines of code between the real and the fake time event loop.\n\n\n## Installation\n\ntimeless_loop is available on PyPI and can be installed with `poetry`, `pip`, or your favorite package manager.\n\n```bash\npip install timeless_loop\n```\n\n## Usage\n\nThe recommended way of setting the TimelessEventLoop is through setring the loop policy with `asyncio.set_event_loop_policy`. It can be used as follows:\n\n```python\nimport asyncio\n\nasync def main():\n    # code here will run on the TimelessEventLoop\n    pass\n\nif __name__ == "__main__":\n    \n    \n    # Set the event loop policy to use the TimelessEventLoop\n    from timeless_loop import TimelessEventLoopPolicy\n    \n    asyncio.set_event_loop_policy(TimelessEventLoopPolicy())\n    asyncio.run(main())\n    \n    # OR:\n    # Use the context manager:\n    import timeless_loop\n    \n    with timeless_loop:\n        asyncio.run(main())\n\n```\n\n## License\n\ntimeless_loop is licensed under the MIT License. See the LICENSE file for more details.\n',
    'author': 'Pedro Batista',
    'author_email': 'pedrovhb@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
