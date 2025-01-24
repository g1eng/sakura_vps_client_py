# ServerMonitoringSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | 監視のON/OFF * true 監視ON * false 監視OFF | 
**health_check** | [**ServerMonitoringSettingsHealthCheck**](ServerMonitoringSettingsHealthCheck.md) |  | 
**notification** | [**ServerMonitoringSettingsNotification**](ServerMonitoringSettingsNotification.md) |  | 

## Example

```python
from sakura_vps_client_py.models.server_monitoring_settings import ServerMonitoringSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ServerMonitoringSettings from a JSON string
server_monitoring_settings_instance = ServerMonitoringSettings.from_json(json)
# print the JSON string representation of the object
print(ServerMonitoringSettings.to_json())

# convert the object into a dict
server_monitoring_settings_dict = server_monitoring_settings_instance.to_dict()
# create an instance of ServerMonitoringSettings from a dict
server_monitoring_settings_from_dict = ServerMonitoringSettings.from_dict(server_monitoring_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


