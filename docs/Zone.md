# Zone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | 
**code** | **str** | ゾーンコード * tk1 東京第1 * tk2 東京第2 * tk3 東京第3 * os1 大阪第1 * os2 大阪第2 * os3 大阪第3 * is1 石狩第1 | 
**name** | **str** | ゾーン名称 | 
**can_use_local** | **bool** | ローカルネットワーク接続が可能かどうか | 
**can_use_hybrid** | **bool** | ハイブリッド接続が利用可能かどうか | 

## Example

```python
from sakura_vps_client_py.models.zone import Zone

# TODO update the JSON string below
json = "{}"
# create an instance of Zone from a JSON string
zone_instance = Zone.from_json(json)
# print the JSON string representation of the object
print(Zone.to_json())

# convert the object into a dict
zone_dict = zone_instance.to_dict()
# create an instance of Zone from a dict
zone_from_dict = Zone.from_dict(zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


