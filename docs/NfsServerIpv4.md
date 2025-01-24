# NfsServerIpv4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | アドレス | 
**netmask** | **str** | サブネットマスク | 

## Example

```python
from sakura_vps_client_py.models.nfs_server_ipv4 import NfsServerIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of NfsServerIpv4 from a JSON string
nfs_server_ipv4_instance = NfsServerIpv4.from_json(json)
# print the JSON string representation of the object
print(NfsServerIpv4.to_json())

# convert the object into a dict
nfs_server_ipv4_dict = nfs_server_ipv4_instance.to_dict()
# create an instance of NfsServerIpv4 from a dict
nfs_server_ipv4_from_dict = NfsServerIpv4.from_dict(nfs_server_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


