# xivo-provd-client [![Build Status](https://jenkins.wazo.community/buildStatus/icon?job=xivo-provd-client)](https://jenkins.wazo.community/job/xivo-provd-client)

A python library to access the REST API of xivo-provd.

## Deprecated

Use wazo-provd-client instead.

## Usage

```python
from xivo_provd_client import new_provisioning_client

provd_client = new_provisioning_client('http://provd.example.com:8666/provd')
dev_mgr = provd_client.device_manager()

print dev_mgr.find({'mac': '00:11:22:33:44:55'})
```

Running unit tests
------------------

```
pip install tox
tox --recreate -e py27
```
