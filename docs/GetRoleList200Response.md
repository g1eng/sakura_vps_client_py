# GetRoleList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | データ総数 | 
**next** | **str** | 次のページへのURL | 
**previous** | **str** | 前のページへのURL | 
**results** | [**List[Role]**](Role.md) |  | 

## Example

```python
from sakura_vps_client_py.models.get_role_list200_response import GetRoleList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoleList200Response from a JSON string
get_role_list200_response_instance = GetRoleList200Response.from_json(json)
# print the JSON string representation of the object
print(GetRoleList200Response.to_json())

# convert the object into a dict
get_role_list200_response_dict = get_role_list200_response_instance.to_dict()
# create an instance of GetRoleList200Response from a dict
get_role_list200_response_from_dict = GetRoleList200Response.from_dict(get_role_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


