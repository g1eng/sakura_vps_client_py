# GetServerList403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | エラー内容を示す簡潔な識別子 | [optional] 
**message** | **str** | エラーの内容 | [optional] 

## Example

```python
from sakura_vps_client_py.models.get_server_list403_response import GetServerList403Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServerList403Response from a JSON string
get_server_list403_response_instance = GetServerList403Response.from_json(json)
# print the JSON string representation of the object
print(GetServerList403Response.to_json())

# convert the object into a dict
get_server_list403_response_dict = get_server_list403_response_instance.to_dict()
# create an instance of GetServerList403Response from a dict
get_server_list403_response_from_dict = GetServerList403Response.from_dict(get_server_list403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


