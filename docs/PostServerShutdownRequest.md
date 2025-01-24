# PostServerShutdownRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | 強制停止を行うか | [optional] [default to False]

## Example

```python
from sakura_vps_client_py.models.post_server_shutdown_request import PostServerShutdownRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServerShutdownRequest from a JSON string
post_server_shutdown_request_instance = PostServerShutdownRequest.from_json(json)
# print the JSON string representation of the object
print(PostServerShutdownRequest.to_json())

# convert the object into a dict
post_server_shutdown_request_dict = post_server_shutdown_request_instance.to_dict()
# create an instance of PostServerShutdownRequest from a dict
post_server_shutdown_request_from_dict = PostServerShutdownRequest.from_dict(post_server_shutdown_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


