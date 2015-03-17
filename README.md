# xivo-provd-client

A python library to access the REST API of xivo-provd.

## Usage

```python
from xivo_provd_client import new_provisioning_client

provd_client = new_provisioning_client('http://provd.example.com:8666/provd')
dev_mgr = provd_client.device_manager()

print dev_mgr.find({'mac': '00:11:22:33:44:55'})
```
