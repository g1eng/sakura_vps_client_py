# SwitchExternalConnection

接続されている外部接続の情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_code** | **str** | サービスコード | [readonly] 
**type** | **str** | 外部接続方式 | [readonly] 
**services** | [**List[SwitchExternalConnectionServicesInner]**](SwitchExternalConnectionServicesInner.md) |  | [readonly] 

## Example

```python
from sakura_vps_client_py.models.switch_external_connection import SwitchExternalConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchExternalConnection from a JSON string
switch_external_connection_instance = SwitchExternalConnection.from_json(json)
# print the JSON string representation of the object
print(SwitchExternalConnection.to_json())

# convert the object into a dict
switch_external_connection_dict = switch_external_connection_instance.to_dict()
# create an instance of SwitchExternalConnection from a dict
switch_external_connection_from_dict = SwitchExternalConnection.from_dict(switch_external_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


