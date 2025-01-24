# GetServerVideoDevice200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | ビデオデバイスの種類 | 

## Example

```python
from sakura_vps_client_py.models.get_server_video_device200_response import GetServerVideoDevice200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServerVideoDevice200Response from a JSON string
get_server_video_device200_response_instance = GetServerVideoDevice200Response.from_json(json)
# print the JSON string representation of the object
print(GetServerVideoDevice200Response.to_json())

# convert the object into a dict
get_server_video_device200_response_dict = get_server_video_device200_response_instance.to_dict()
# create an instance of GetServerVideoDevice200Response from a dict
get_server_video_device200_response_from_dict = GetServerVideoDevice200Response.from_dict(get_server_video_device200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


