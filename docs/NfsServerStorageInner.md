# NfsServerStorageInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 種別 | 
**size_gibibytes** | **int** | ストレージ容量(GiB) | 

## Example

```python
from sakura_vps_client_py.models.nfs_server_storage_inner import NfsServerStorageInner

# TODO update the JSON string below
json = "{}"
# create an instance of NfsServerStorageInner from a JSON string
nfs_server_storage_inner_instance = NfsServerStorageInner.from_json(json)
# print the JSON string representation of the object
print(NfsServerStorageInner.to_json())

# convert the object into a dict
nfs_server_storage_inner_dict = nfs_server_storage_inner_instance.to_dict()
# create an instance of NfsServerStorageInner from a dict
nfs_server_storage_inner_from_dict = NfsServerStorageInner.from_dict(nfs_server_storage_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


