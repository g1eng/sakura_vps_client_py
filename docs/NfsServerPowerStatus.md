# NfsServerPowerStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | 電源ステータス * power_on 電源ON * in_shutdown シャットダウン中 * power_off 電源OFF * unknown 不明（電源状態を取得できない） | 

## Example

```python
from sakura_vps_client_py.models.nfs_server_power_status import NfsServerPowerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NfsServerPowerStatus from a JSON string
nfs_server_power_status_instance = NfsServerPowerStatus.from_json(json)
# print the JSON string representation of the object
print(NfsServerPowerStatus.to_json())

# convert the object into a dict
nfs_server_power_status_dict = nfs_server_power_status_instance.to_dict()
# create an instance of NfsServerPowerStatus from a dict
nfs_server_power_status_from_dict = NfsServerPowerStatus.from_dict(nfs_server_power_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


