# SwitchExternalConnectionServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_category** | **str** | サービスカテゴリー | [readonly] 
**service_name** | **str** | サービス名 | [readonly] 
**switch_code** | **str** | スイッチコード | [readonly] 

## Example

```python
from sakura_vps_client_py.models.switch_external_connection_services_inner import SwitchExternalConnectionServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchExternalConnectionServicesInner from a JSON string
switch_external_connection_services_inner_instance = SwitchExternalConnectionServicesInner.from_json(json)
# print the JSON string representation of the object
print(SwitchExternalConnectionServicesInner.to_json())

# convert the object into a dict
switch_external_connection_services_inner_dict = switch_external_connection_services_inner_instance.to_dict()
# create an instance of SwitchExternalConnectionServicesInner from a dict
switch_external_connection_services_inner_from_dict = SwitchExternalConnectionServicesInner.from_dict(switch_external_connection_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


