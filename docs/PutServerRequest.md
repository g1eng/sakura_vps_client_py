# PutServerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 名前 | 
**description** | **str** | 説明 | 

## Example

```python
from sakura_vps_client_py.models.put_server_request import PutServerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutServerRequest from a JSON string
put_server_request_instance = PutServerRequest.from_json(json)
# print the JSON string representation of the object
print(PutServerRequest.to_json())

# convert the object into a dict
put_server_request_dict = put_server_request_instance.to_dict()
# create an instance of PutServerRequest from a dict
put_server_request_from_dict = PutServerRequest.from_dict(put_server_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


