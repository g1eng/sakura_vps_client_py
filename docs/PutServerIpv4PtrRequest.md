# PutServerIpv4PtrRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | ホスト名 | 

## Example

```python
from sakura_vps_client_py.models.put_server_ipv4_ptr_request import PutServerIpv4PtrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutServerIpv4PtrRequest from a JSON string
put_server_ipv4_ptr_request_instance = PutServerIpv4PtrRequest.from_json(json)
# print the JSON string representation of the object
print(PutServerIpv4PtrRequest.to_json())

# convert the object into a dict
put_server_ipv4_ptr_request_dict = put_server_ipv4_ptr_request_instance.to_dict()
# create an instance of PutServerIpv4PtrRequest from a dict
put_server_ipv4_ptr_request_from_dict = PutServerIpv4PtrRequest.from_dict(put_server_ipv4_ptr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


