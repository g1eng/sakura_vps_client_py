# InvalidParameterDetailInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | エラー内容を示す簡潔な識別子 | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from sakura_vps_client_py.models.invalid_parameter_detail_inner import InvalidParameterDetailInner

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidParameterDetailInner from a JSON string
invalid_parameter_detail_inner_instance = InvalidParameterDetailInner.from_json(json)
# print the JSON string representation of the object
print(InvalidParameterDetailInner.to_json())

# convert the object into a dict
invalid_parameter_detail_inner_dict = invalid_parameter_detail_inner_instance.to_dict()
# create an instance of InvalidParameterDetailInner from a dict
invalid_parameter_detail_inner_from_dict = InvalidParameterDetailInner.from_dict(invalid_parameter_detail_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


