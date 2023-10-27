# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['transmit', 'transmit.trans']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0',
 'pretty-errors>=1.2.25,<2.0.0',
 'pydantic>=2.4.2,<3.0.0',
 'thrift>=0.15.0,<0.16.0']

setup_kwargs = {
    'name': 'transmit',
    'version': '0.3.0',
    'description': 'Transmit Server & Client use thrift',
    'long_description': '# Transmit Server & Client\n\n## Install\n\n```\npip install transmit\n```\n\n## Usage\n\n### Server\n\n```\nfrom transmit.server import Server\n\nclass TestServer(Server):\n    def __init__(self,port=18100):\n        super().__init__(port)\n\n    def test_function(self,msg):\n        print(\'Testing:\',msg)\n        return {"say":"Happy everyday!!!"}\n\nif __name__ == \'__main__\':\n    ts = TestServer()\n    ts.run()\n\n```\n\n> Result\n\n```shell\nSTART SERVER 0.0.0.0:18100\n\n```\n\n#### Success Response\n\n```\n{\n    "code":1,\n    "msg":"success",\n    "data":"handle result data. AnyType"\n}\n```\n\n#### Error Response\n\n```\n{\n    "code":0,\n    "msg":"error message",\n    "data":null\n}\n```\n\n### Client\n\n```\nfrom transmit.client import Client\n\nwith Client("127.0.0.1",18100) as c:\n    result = c.test_function({"msg":"hello world"})\n    print(type(result))\n    print(result)\n\n```\n\n> Result\n\n```shell\n> <class \'dict\'>\n> {\'say\': \'Happy everyday!!!\'}\n```\n\n### Advanced Usage\n\n1. debug mode\n\ndebug mode will print and log all request and response data.\n\n```shell\n# debug server\n> python test_server.py --debug 1\n```\n\n```python\n# debug client\nwith Client("127.0.0.1",18100,debug=True) as c:\n    ...\n```\n\n2. server cli setting\n\n```shell\n> python test_server.py --host "127.0.0.1" --port 3000 --debug 1\n```\n\n### Refs\n\n[Thrift](https://thrift.apache.org/)\n\n```\n\n```\n',
    'author': 'hbh112233abc',
    'author_email': 'hbh112233abc@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hbh112233abc/py-transmit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
