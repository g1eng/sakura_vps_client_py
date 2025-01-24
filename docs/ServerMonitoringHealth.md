# ServerMonitoringHealth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_checked_at** | **datetime** | 最終監視日時 | 
**status** | **str** | ステータス   * healthy 正常   * unhealthy 異常 | 
**last_status_changed_at** | **datetime** | 最終ステータス変更日時 | 

## Example

```python
from sakura_vps_client_py.models.server_monitoring_health import ServerMonitoringHealth

# TODO update the JSON string below
json = "{}"
# create an instance of ServerMonitoringHealth from a JSON string
server_monitoring_health_instance = ServerMonitoringHealth.from_json(json)
# print the JSON string representation of the object
print(ServerMonitoringHealth.to_json())

# convert the object into a dict
server_monitoring_health_dict = server_monitoring_health_instance.to_dict()
# create an instance of ServerMonitoringHealth from a dict
server_monitoring_health_from_dict = ServerMonitoringHealth.from_dict(server_monitoring_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


