# ServerMonitoring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | [readonly] 
**name** | **str** | 名前 | 
**description** | **str** | 説明 | 
**monitoring_resource_id** | **str** | 監視リソースID | [readonly] 
**update_status** | **str** | 更新ステータス * waiting 更新待ち * updating 更新中 * completed 更新完了 * error 更新エラー | [readonly] 
**settings** | [**ServerMonitoringSettings**](ServerMonitoringSettings.md) |  | 

## Example

```python
from sakura_vps_client_py.models.server_monitoring import ServerMonitoring

# TODO update the JSON string below
json = "{}"
# create an instance of ServerMonitoring from a JSON string
server_monitoring_instance = ServerMonitoring.from_json(json)
# print the JSON string representation of the object
print(ServerMonitoring.to_json())

# convert the object into a dict
server_monitoring_dict = server_monitoring_instance.to_dict()
# create an instance of ServerMonitoring from a dict
server_monitoring_from_dict = ServerMonitoring.from_dict(server_monitoring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


