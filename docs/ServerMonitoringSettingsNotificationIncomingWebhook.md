# ServerMonitoringSettingsNotificationIncomingWebhook

incoming webhookでの通知の設定

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | 通知のON/OFF * true 通知ON * false 通知OFF | 
**webhooks_url** | **str** | 通知先のWebhooksURL。 Slack、Discord、Microsoft TeamsのIncoming WebHooksにのみ対応しています。 指定できるURLは各サービスのWebhook URL(https://hooks.slack.com/services/* など)の形式に制限されています。 Discordの場合は[Slack互換のWebhook URL](https://discord.com/developers/docs/resources/webhook#execute-slackcompatible-webhook)を指定してください。 | 
**slack_team_name** | **str** | slackのteam name。VPSコントロールパネルの「Slackと自動で連携をする」を利用した場合に設定されます。 | [readonly] 
**slack_channel_name** | **str** | slackのchannel name。VPSコントロールパネルの「Slackと自動で連携をする」を利用した場合に設定されます。 | [readonly] 

## Example

```python
from sakura_vps_client_py.models.server_monitoring_settings_notification_incoming_webhook import ServerMonitoringSettingsNotificationIncomingWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of ServerMonitoringSettingsNotificationIncomingWebhook from a JSON string
server_monitoring_settings_notification_incoming_webhook_instance = ServerMonitoringSettingsNotificationIncomingWebhook.from_json(json)
# print the JSON string representation of the object
print(ServerMonitoringSettingsNotificationIncomingWebhook.to_json())

# convert the object into a dict
server_monitoring_settings_notification_incoming_webhook_dict = server_monitoring_settings_notification_incoming_webhook_instance.to_dict()
# create an instance of ServerMonitoringSettingsNotificationIncomingWebhook from a dict
server_monitoring_settings_notification_incoming_webhook_from_dict = ServerMonitoringSettingsNotificationIncomingWebhook.from_dict(server_monitoring_settings_notification_incoming_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


