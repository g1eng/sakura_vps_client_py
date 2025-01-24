# SwitchZone

ゾーン情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | ゾーンコード * tk1 東京第1 * tk2 東京第2 * tk3 東京第3 * os1 大阪第1 * os2 大阪第2 * os3 大阪第3 * is1 石狩第1 | [readonly] 
**name** | **str** | ゾーン名称 | [readonly] 

## Example

```python
from sakura_vps_client_py.models.switch_zone import SwitchZone

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchZone from a JSON string
switch_zone_instance = SwitchZone.from_json(json)
# print the JSON string representation of the object
print(SwitchZone.to_json())

# convert the object into a dict
switch_zone_dict = switch_zone_instance.to_dict()
# create an instance of SwitchZone from a dict
switch_zone_from_dict = SwitchZone.from_dict(switch_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


