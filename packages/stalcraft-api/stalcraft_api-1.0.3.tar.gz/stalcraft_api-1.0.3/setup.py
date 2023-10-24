# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stalcraft',
 'stalcraft.api',
 'stalcraft.asyncio',
 'stalcraft.asyncio.api',
 'stalcraft.asyncio.auction',
 'stalcraft.asyncio.auth',
 'stalcraft.asyncio.clan',
 'stalcraft.asyncio.client',
 'stalcraft.auction',
 'stalcraft.auth',
 'stalcraft.clan',
 'stalcraft.client',
 'stalcraft.items',
 'stalcraft.schemas',
 'stalcraft.utils']

package_data = \
{'': ['*'], 'stalcraft.items': ['listing/global/*', 'listing/ru/*']}

install_requires = \
['httpx>=0.25.0,<0.26.0', 'pydantic>=1.10.0,<2.0.0']

setup_kwargs = {
    'name': 'stalcraft-api',
    'version': '1.0.3',
    'description': 'stalcraft api unofficial python library',
    'long_description': '<h1 align="center">stalcraft-api unofficial python library</h1>\n\n<p align="center">\n    <a href="https://pypi.org/project/stalcraft-api" alt="PyPi Package Version">\n        <img src="https://img.shields.io/pypi/v/stalcraft-api.svg?style=flat-square"/>\n    </a>\n    <a href="https://pypi.org/project/stalcraft-api" alt="Supported python versions">\n        <img src="https://img.shields.io/pypi/pyversions/stalcraft-api.svg?style=flat-square"/>\n    </a>\n    <a href="https://opensource.org/licenses/MIT" alt="MIT License">\n        <img src="https://img.shields.io/pypi/l/aiogram.svg?style=flat-squar"/>\n    </a>\n</p>\n\n\n<br>\n\n<p align="center">\n    <b>Official API documentation:</b> https://eapi.stalcraft.net\n</p>\n<p align="center">\n    <b>Before you can use the API, you must register your application and receive approval<b>\n</p>\n<p align="center">\n    <b>For testing Demo API is available<b>\n</p>\n<p align="center">\n    <a href="https://eapi.stalcraft.net/registration.html">more about applications</a>\n</p>\n\n\n<br>\n\n# 🔧 Install\n\n### Pip\n\n```console\npip install stalcraft-api -U\n```\n\n<details>\n<summary>Manual</summary>\n\n```console\ngit clone git@github.com:onejeuu/stalcraft-api.git\n```\n\n```console\ncd stalcraft-api\n```\n\n```console\npoetry install\n```\n</details>\n\n\n<br>\n\n# ⚡ Quick Start\n\n```python\nfrom stalcraft import AppClient, Region\n\n# Only as example.\n# Do not store your credentials in code.\nTOKEN = "YOUR_TOKEN"\n\nclient = AppClient(token=TOKEN)\n\nprint(client.emission(Region.EU))\n```\n\n<details>\n<summary>🐇 Asyncio</summary>\n\n```python\nfrom stalcraft.asyncio import AsyncAppClient\nfrom stalcraft import Region\nimport asyncio\n\nTOKEN = "YOUR_TOKEN"\n\nasync def main():\n    client = AsyncAppClient(token=TOKEN)\n\n    print(await client.emission(Region.EU))\n\nasyncio.run(main())\n```\n\n</details>\n\n<br>\n\n\n# 🚫 Exceptions\n\n```\nStalcraftApiException\n├── InvalidToken\n├── MissingCredentials\n├── ApiRequestError\n│   ├── RequestUnauthorised\n│   ├── RequestInvalidParameter\n│   ├── RequestNotFound\n│   └── RateLimitReached\n└── ItemIdError\n    ├── ListingJsonNotFound\n    └── ItemIdNotFound\n```\n\n<br>\n\n# 🔑 Authorization\n\n```python\nfrom stalcraft import AppAuth, UserAuth\n\n# Only as example.\n# Do not store your credentials in code.\nCLIENT_ID = "YOUR_CLIENT_ID"\nCLIENT_SECRET = "YOUR_CLIENT_SECRET"\n\napp_auth = AppAuth(CLIENT_ID, CLIENT_SECRET)\nuser_auth = UserAuth(CLIENT_ID, CLIENT_SECRET)\n```\n\n<details>\n<summary>Get App Token</summary>\n\n```python\nprint(app_auth.get_token())\n```\n\n</details>\n\n<br>\n\n<details>\n<summary>Get User Token</summary>\n\n```python\nprint(user_auth.code_url)\n\ncode = input("Enter code:")\n\nprint()\nprint(user_auth.get_token(code))\n```\n\n</details>\n\n<br>\n\n<details>\n<summary>Refresh User Token</summary>\n\n```python\nREFRESH_TOKEN = "USER_REFRESH_TOKEN"\n\nprint(user_auth.refresh_token(REFRESH_TOKEN))\n```\n\n</details>\n\n\n<br>\n\n# 📋 Output Formats\n\n```python\nfrom stalcraft import AppClient\n\nTOKEN = "YOUR_TOKEN"\n\nclient = AppClient(token=TOKEN)\n\nprint("Object:")\nprint(client.emission())\n\nclient = AppClient(TOKEN, json=True)\n\n# or\n# client.json = True\n\nprint()\nprint("Json:")\nprint(client.emission())\n```\n\n### Output:\n\n```python\nObject:\nEmission(\n    current_start=None,\n    previous_start=datetime.datetime(2023, 1, 30, 12, 0, 0, tzinfo=datetime.timezone.utc),\n    previous_end=datetime.datetime(2023, 1, 30, 12, 5, 0, tzinfo=datetime.timezone.utc)\n)\n\nJson:\n{\n    \'previousStart\': \'2023-01-30T12:00:00Z\',\n    \'previousEnd\': \'2023-01-30T12:05:00Z\'\n}\n```\n',
    'author': 'onejeuu',
    'author_email': 'bloodtrail@beber1k.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
