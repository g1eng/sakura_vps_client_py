# NfsServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | 
**name** | **str** | 名前 | 
**description** | **str** | 説明 | 
**service_status** | **str** | サービス状況 * in_preparation 準備中 * on_trial お試し中 * link_down_on_trial お試し中（一時停止） * in_use 利用中 * link_down 一時停止中 | 
**setting_status** | **str** | 設定状況 * done 設定完了 * in_update 設定更新中 * failed 設定更新失敗 | 
**storage** | [**List[NfsServerStorageInner]**](NfsServerStorageInner.md) | ストレージ情報 | 
**zone** | [**ServerZone**](ServerZone.md) |  | 
**ipv4** | [**NfsServerIpv4**](NfsServerIpv4.md) |  | 
**contract** | [**NfsServerContract**](NfsServerContract.md) |  | 
**power_status** | **str** | 電源ステータス * power_on 電源ON * in_shutdown シャットダウン中 * power_off 電源OFF * unknown 不明（電源状態を取得できない） このエンドポイントが返す電源ステータスはキャッシュされた情報のため、最新の正確な電源ステータスではない場合があります | 

## Example

```python
from sakura_vps_client_py.models.nfs_server import NfsServer

# TODO update the JSON string below
json = "{}"
# create an instance of NfsServer from a JSON string
nfs_server_instance = NfsServer.from_json(json)
# print the JSON string representation of the object
print(NfsServer.to_json())

# convert the object into a dict
nfs_server_dict = nfs_server_instance.to_dict()
# create an instance of NfsServer from a dict
nfs_server_from_dict = NfsServer.from_dict(nfs_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


