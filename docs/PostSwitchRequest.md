# PostSwitchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 名前 | 
**description** | **str** | 説明 | 
**zone_code** | **str** | ゾーンコード * tk2 東京第2 * tk3 東京第3 * os3 大阪第3 * is1 石狩第1 | 

## Example

```python
from sakura_vps_client_py.models.post_switch_request import PostSwitchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSwitchRequest from a JSON string
post_switch_request_instance = PostSwitchRequest.from_json(json)
# print the JSON string representation of the object
print(PostSwitchRequest.to_json())

# convert the object into a dict
post_switch_request_dict = post_switch_request_instance.to_dict()
# create an instance of PostSwitchRequest from a dict
post_switch_request_from_dict = PostSwitchRequest.from_dict(post_switch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


