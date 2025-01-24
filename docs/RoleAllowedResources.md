# RoleAllowedResources

利用できるリソース。resource_filteringがenabledの場合のみ指定可能。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | **List[int]** | 利用できるサーバーのid | [optional] 
**switches** | **List[int]** | 利用できるスイッチのid | [optional] 
**nfs_servers** | **List[int]** | 利用できるNFSのid | [optional] 

## Example

```python
from sakura_vps_client_py.models.role_allowed_resources import RoleAllowedResources

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAllowedResources from a JSON string
role_allowed_resources_instance = RoleAllowedResources.from_json(json)
# print the JSON string representation of the object
print(RoleAllowedResources.to_json())

# convert the object into a dict
role_allowed_resources_dict = role_allowed_resources_instance.to_dict()
# create an instance of RoleAllowedResources from a dict
role_allowed_resources_from_dict = RoleAllowedResources.from_dict(role_allowed_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


