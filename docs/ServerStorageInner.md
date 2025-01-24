# ServerStorageInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | ポート番号 | 
**type** | **str** | 種別 | 
**size_gibibytes** | **int** | ストレージ容量(GiB) | 

## Example

```python
from sakura_vps_client_py.models.server_storage_inner import ServerStorageInner

# TODO update the JSON string below
json = "{}"
# create an instance of ServerStorageInner from a JSON string
server_storage_inner_instance = ServerStorageInner.from_json(json)
# print the JSON string representation of the object
print(ServerStorageInner.to_json())

# convert the object into a dict
server_storage_inner_dict = server_storage_inner_instance.to_dict()
# create an instance of ServerStorageInner from a dict
server_storage_inner_from_dict = ServerStorageInner.from_dict(server_storage_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


