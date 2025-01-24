# HealthCheckPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | 監視方法 | 
**interval_minutes** | **int** | チェック間隔(分) | 

## Example

```python
from sakura_vps_client_py.models.health_check_ping import HealthCheckPing

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckPing from a JSON string
health_check_ping_instance = HealthCheckPing.from_json(json)
# print the JSON string representation of the object
print(HealthCheckPing.to_json())

# convert the object into a dict
health_check_ping_dict = health_check_ping_instance.to_dict()
# create an instance of HealthCheckPing from a dict
health_check_ping_from_dict = HealthCheckPing.from_dict(health_check_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


