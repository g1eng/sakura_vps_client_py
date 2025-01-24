# Disc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | 
**name** | **str** | 名前 | 
**description** | **str** | 説明 | 
**license_required** | **bool** | ライセンスが必要かどうか | 

## Example

```python
from sakura_vps_client_py.models.disc import Disc

# TODO update the JSON string below
json = "{}"
# create an instance of Disc from a JSON string
disc_instance = Disc.from_json(json)
# print the JSON string representation of the object
print(Disc.to_json())

# convert the object into a dict
disc_dict = disc_instance.to_dict()
# create an instance of Disc from a dict
disc_from_dict = Disc.from_dict(disc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


