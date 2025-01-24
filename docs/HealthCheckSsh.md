# HealthCheckSsh


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | 監視方法 | 
**port** | **int** | ポート番号 | 
**interval_minutes** | **int** | チェック間隔(分) | 

## Example

```python
from sakura_vps_client_py.models.health_check_ssh import HealthCheckSsh

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckSsh from a JSON string
health_check_ssh_instance = HealthCheckSsh.from_json(json)
# print the JSON string representation of the object
print(HealthCheckSsh.to_json())

# convert the object into a dict
health_check_ssh_dict = health_check_ssh_instance.to_dict()
# create an instance of HealthCheckSsh from a dict
health_check_ssh_from_dict = HealthCheckSsh.from_dict(health_check_ssh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


