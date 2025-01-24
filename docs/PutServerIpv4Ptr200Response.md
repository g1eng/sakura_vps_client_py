# PutServerIpv4Ptr200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ptr** | **str** | 逆引きホスト名 | 

## Example

```python
from sakura_vps_client_py.models.put_server_ipv4_ptr200_response import PutServerIpv4Ptr200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PutServerIpv4Ptr200Response from a JSON string
put_server_ipv4_ptr200_response_instance = PutServerIpv4Ptr200Response.from_json(json)
# print the JSON string representation of the object
print(PutServerIpv4Ptr200Response.to_json())

# convert the object into a dict
put_server_ipv4_ptr200_response_dict = put_server_ipv4_ptr200_response_instance.to_dict()
# create an instance of PutServerIpv4Ptr200Response from a dict
put_server_ipv4_ptr200_response_from_dict = PutServerIpv4Ptr200Response.from_dict(put_server_ipv4_ptr200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


