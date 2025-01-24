# PostServerMountDiscRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disc_id** | **int** | ディスクID | 

## Example

```python
from sakura_vps_client_py.models.post_server_mount_disc_request import PostServerMountDiscRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServerMountDiscRequest from a JSON string
post_server_mount_disc_request_instance = PostServerMountDiscRequest.from_json(json)
# print the JSON string representation of the object
print(PostServerMountDiscRequest.to_json())

# convert the object into a dict
post_server_mount_disc_request_dict = post_server_mount_disc_request_instance.to_dict()
# create an instance of PostServerMountDiscRequest from a dict
post_server_mount_disc_request_from_dict = PostServerMountDiscRequest.from_dict(post_server_mount_disc_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


