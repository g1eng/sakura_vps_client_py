# PostSwitch201ResponseZone

ゾーン情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | ゾーンコード * tk2 東京第2 * tk3 東京第3 * os3 大阪第3 * is1 石狩第1 | [readonly] 
**name** | **str** | ゾーン名称 | [readonly] 

## Example

```python
from sakura_vps_client_py.models.post_switch201_response_zone import PostSwitch201ResponseZone

# TODO update the JSON string below
json = "{}"
# create an instance of PostSwitch201ResponseZone from a JSON string
post_switch201_response_zone_instance = PostSwitch201ResponseZone.from_json(json)
# print the JSON string representation of the object
print(PostSwitch201ResponseZone.to_json())

# convert the object into a dict
post_switch201_response_zone_dict = post_switch201_response_zone_instance.to_dict()
# create an instance of PostSwitch201ResponseZone from a dict
post_switch201_response_zone_from_dict = PostSwitch201ResponseZone.from_dict(post_switch201_response_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


