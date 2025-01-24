# PutServerVideoDeviceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | ビデオデバイスの種類 | 

## Example

```python
from sakura_vps_client_py.models.put_server_video_device_request import PutServerVideoDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutServerVideoDeviceRequest from a JSON string
put_server_video_device_request_instance = PutServerVideoDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(PutServerVideoDeviceRequest.to_json())

# convert the object into a dict
put_server_video_device_request_dict = put_server_video_device_request_instance.to_dict()
# create an instance of PutServerVideoDeviceRequest from a dict
put_server_video_device_request_from_dict = PutServerVideoDeviceRequest.from_dict(put_server_video_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


