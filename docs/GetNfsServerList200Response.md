# GetNfsServerList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | データ総数 | 
**next** | **str** | 次のページへのURL | 
**previous** | **str** | 前のページへのURL | 
**results** | [**List[NfsServer]**](NfsServer.md) |  | 

## Example

```python
from sakura_vps_client_py.models.get_nfs_server_list200_response import GetNfsServerList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNfsServerList200Response from a JSON string
get_nfs_server_list200_response_instance = GetNfsServerList200Response.from_json(json)
# print the JSON string representation of the object
print(GetNfsServerList200Response.to_json())

# convert the object into a dict
get_nfs_server_list200_response_dict = get_nfs_server_list200_response_instance.to_dict()
# create an instance of GetNfsServerList200Response from a dict
get_nfs_server_list200_response_from_dict = GetNfsServerList200Response.from_dict(get_nfs_server_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


