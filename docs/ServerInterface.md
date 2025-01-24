# ServerInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | [readonly] 
**device** | **str** | NIC名称 | [readonly] 
**connectable_to_global_network** | **bool** | グローバルネットワークと接続可能か | [readonly] 
**connect_to** | **str** | インターフェースの接続先 | [readonly] 
**mac** | **str** | MACアドレス | [readonly] 
**switch_id** | **int** | スイッチID | 

## Example

```python
from sakura_vps_client_py.models.server_interface import ServerInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ServerInterface from a JSON string
server_interface_instance = ServerInterface.from_json(json)
# print the JSON string representation of the object
print(ServerInterface.to_json())

# convert the object into a dict
server_interface_dict = server_interface_instance.to_dict()
# create an instance of ServerInterface from a dict
server_interface_from_dict = ServerInterface.from_dict(server_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


