# GetServerList401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | エラー内容を示す簡潔な識別子 | [optional] 
**message** | **str** | エラーの内容 | [optional] 

## Example

```python
from sakura_vps_client_py.models.get_server_list401_response import GetServerList401Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServerList401Response from a JSON string
get_server_list401_response_instance = GetServerList401Response.from_json(json)
# print the JSON string representation of the object
print(GetServerList401Response.to_json())

# convert the object into a dict
get_server_list401_response_dict = get_server_list401_response_instance.to_dict()
# create an instance of GetServerList401Response from a dict
get_server_list401_response_from_dict = GetServerList401Response.from_dict(get_server_list401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


