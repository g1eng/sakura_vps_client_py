# Keymap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout** | **str** | 指定したいキー配列の名称 | 

## Example

```python
from sakura_vps_client_py.models.keymap import Keymap

# TODO update the JSON string below
json = "{}"
# create an instance of Keymap from a JSON string
keymap_instance = Keymap.from_json(json)
# print the JSON string representation of the object
print(Keymap.to_json())

# convert the object into a dict
keymap_dict = keymap_instance.to_dict()
# create an instance of Keymap from a dict
keymap_from_dict = Keymap.from_dict(keymap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


