# HealthCheckSmtp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | 監視方法 | 
**port** | **int** | ポート番号 | 
**interval_minutes** | **int** | チェック間隔(分) | 

## Example

```python
from sakura_vps_client_py.models.health_check_smtp import HealthCheckSmtp

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckSmtp from a JSON string
health_check_smtp_instance = HealthCheckSmtp.from_json(json)
# print the JSON string representation of the object
print(HealthCheckSmtp.to_json())

# convert the object into a dict
health_check_smtp_dict = health_check_smtp_instance.to_dict()
# create an instance of HealthCheckSmtp from a dict
health_check_smtp_from_dict = HealthCheckSmtp.from_dict(health_check_smtp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


