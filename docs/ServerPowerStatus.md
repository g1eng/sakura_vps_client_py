# ServerPowerStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | 電源ステータス * power_on 電源ON * in_shutdown シャットダウン中 * power_off 電源OFF * installing OSインストール中 * in_scaleup スケールアップ中 * migration サーバー移行作業中 * unknown 不明（電源状態を取得できない） | 

## Example

```python
from sakura_vps_client_py.models.server_power_status import ServerPowerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPowerStatus from a JSON string
server_power_status_instance = ServerPowerStatus.from_json(json)
# print the JSON string representation of the object
print(ServerPowerStatus.to_json())

# convert the object into a dict
server_power_status_dict = server_power_status_instance.to_dict()
# create an instance of ServerPowerStatus from a dict
server_power_status_from_dict = ServerPowerStatus.from_dict(server_power_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


