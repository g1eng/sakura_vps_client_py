# HealthCheckPop3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | 監視方法 | 
**port** | **int** | ポート番号 | 
**interval_minutes** | **int** | チェック間隔(分) | 

## Example

```python
from sakura_vps_client_py.models.health_check_pop3 import HealthCheckPop3

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckPop3 from a JSON string
health_check_pop3_instance = HealthCheckPop3.from_json(json)
# print the JSON string representation of the object
print(HealthCheckPop3.to_json())

# convert the object into a dict
health_check_pop3_dict = health_check_pop3_instance.to_dict()
# create an instance of HealthCheckPop3 from a dict
health_check_pop3_from_dict = HealthCheckPop3.from_dict(health_check_pop3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


