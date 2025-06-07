# NfsStorageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_space_kib** | **int** | ストレージの空き容量（KiB） | [readonly] 
**usage_percentage** | **int** | ストレージの使用率 | [readonly] 
**capacity_kib** | **int** | ストレージの全容量（KiB） | [readonly] 
**usage_kib** | **int** | ストレージの使用容量（KiB） | [readonly] 

## Example

```python
from sakura_vps_client_py.models.nfs_storage_info import NfsStorageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NfsStorageInfo from a JSON string
nfs_storage_info_instance = NfsStorageInfo.from_json(json)
# print the JSON string representation of the object
print(NfsStorageInfo.to_json())

# convert the object into a dict
nfs_storage_info_dict = nfs_storage_info_instance.to_dict()
# create an instance of NfsStorageInfo from a dict
nfs_storage_info_from_dict = NfsStorageInfo.from_dict(nfs_storage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


