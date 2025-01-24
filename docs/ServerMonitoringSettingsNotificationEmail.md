# ServerMonitoringSettingsNotificationEmail

emailでの通知の設定。会員情報に登録されているメールアドレス宛に送信されます。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | 通知のON/OFF * true 通知ON * false 通知OFF | 

## Example

```python
from sakura_vps_client_py.models.server_monitoring_settings_notification_email import ServerMonitoringSettingsNotificationEmail

# TODO update the JSON string below
json = "{}"
# create an instance of ServerMonitoringSettingsNotificationEmail from a JSON string
server_monitoring_settings_notification_email_instance = ServerMonitoringSettingsNotificationEmail.from_json(json)
# print the JSON string representation of the object
print(ServerMonitoringSettingsNotificationEmail.to_json())

# convert the object into a dict
server_monitoring_settings_notification_email_dict = server_monitoring_settings_notification_email_instance.to_dict()
# create an instance of ServerMonitoringSettingsNotificationEmail from a dict
server_monitoring_settings_notification_email_from_dict = ServerMonitoringSettingsNotificationEmail.from_dict(server_monitoring_settings_notification_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


