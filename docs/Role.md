# Role


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | [readonly] 
**name** | **str** | 名前 | 
**description** | **str** | 説明 | 
**permission_filtering** | **str** | 利用できる権限を制限するか | 
**allowed_permissions** | **List[str]** | 利用できる権限。permission_filteringがenabledの場合のみ指定可能。**権限の一覧を取得する**&#x60;/permissions&#x60;のcode値を指定します。 | 
**resource_filtering** | **str** | 利用できるリソースを制限するか | 
**allowed_resources** | [**RoleAllowedResources**](RoleAllowedResources.md) |  | 

## Example

```python
from sakura_vps_client_py.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print(Role.to_json())

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_from_dict = Role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


