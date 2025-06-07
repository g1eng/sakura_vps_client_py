# NfsServerInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connect_to** | **str** | インターフェースの接続先 | [readonly] 
**mac** | **str** | MACアドレス | [readonly] 
**switch_id** | **int** | スイッチID | 

## Example

```python
from sakura_vps_client_py.models.nfs_server_interface import NfsServerInterface

# TODO update the JSON string below
json = "{}"
# create an instance of NfsServerInterface from a JSON string
nfs_server_interface_instance = NfsServerInterface.from_json(json)
# print the JSON string representation of the object
print(NfsServerInterface.to_json())

# convert the object into a dict
nfs_server_interface_dict = nfs_server_interface_instance.to_dict()
# create an instance of NfsServerInterface from a dict
nfs_server_interface_from_dict = NfsServerInterface.from_dict(nfs_server_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


