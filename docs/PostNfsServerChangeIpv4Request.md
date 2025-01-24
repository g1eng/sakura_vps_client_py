# PostNfsServerChangeIpv4Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | ipv4アドレス | 
**netmask** | **str** | ネットマスク | 

## Example

```python
from sakura_vps_client_py.models.post_nfs_server_change_ipv4_request import PostNfsServerChangeIpv4Request

# TODO update the JSON string below
json = "{}"
# create an instance of PostNfsServerChangeIpv4Request from a JSON string
post_nfs_server_change_ipv4_request_instance = PostNfsServerChangeIpv4Request.from_json(json)
# print the JSON string representation of the object
print(PostNfsServerChangeIpv4Request.to_json())

# convert the object into a dict
post_nfs_server_change_ipv4_request_dict = post_nfs_server_change_ipv4_request_instance.to_dict()
# create an instance of PostNfsServerChangeIpv4Request from a dict
post_nfs_server_change_ipv4_request_from_dict = PostNfsServerChangeIpv4Request.from_dict(post_nfs_server_change_ipv4_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


