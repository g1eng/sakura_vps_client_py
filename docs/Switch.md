# Switch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | [readonly] 
**name** | **str** | 名前 | 
**description** | **str** | 説明 | 
**switch_code** | **str** | スイッチコード | [readonly] 
**zone** | [**SwitchZone**](SwitchZone.md) |  | 
**server_interfaces** | **List[int]** | 接続されているサーバーのインターフェースid | [readonly] 
**nfs_server_interfaces** | **List[int]** | 接続されている追加ストレージ（NFS）のインターフェースid | [readonly] 
**external_connection** | [**SwitchExternalConnection**](SwitchExternalConnection.md) |  | 

## Example

```python
from sakura_vps_client_py.models.switch import Switch

# TODO update the JSON string below
json = "{}"
# create an instance of Switch from a JSON string
switch_instance = Switch.from_json(json)
# print the JSON string representation of the object
print(Switch.to_json())

# convert the object into a dict
switch_dict = switch_instance.to_dict()
# create an instance of Switch from a dict
switch_from_dict = Switch.from_dict(switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


