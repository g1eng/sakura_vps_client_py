# ServerMonitoringSettingsNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**ServerMonitoringSettingsNotificationEmail**](ServerMonitoringSettingsNotificationEmail.md) |  | 
**incoming_webhook** | [**ServerMonitoringSettingsNotificationIncomingWebhook**](ServerMonitoringSettingsNotificationIncomingWebhook.md) |  | 
**interval_hours** | **int** | 再通知間隔(時間) | 

## Example

```python
from sakura_vps_client_py.models.server_monitoring_settings_notification import ServerMonitoringSettingsNotification

# TODO update the JSON string below
json = "{}"
# create an instance of ServerMonitoringSettingsNotification from a JSON string
server_monitoring_settings_notification_instance = ServerMonitoringSettingsNotification.from_json(json)
# print the JSON string representation of the object
print(ServerMonitoringSettingsNotification.to_json())

# convert the object into a dict
server_monitoring_settings_notification_dict = server_monitoring_settings_notification_instance.to_dict()
# create an instance of ServerMonitoringSettingsNotification from a dict
server_monitoring_settings_notification_from_dict = ServerMonitoringSettingsNotification.from_dict(server_monitoring_settings_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


