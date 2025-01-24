# Server


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | 
**name** | **str** | 名前 | 
**description** | **str** | 説明 | 
**service_type** | **str** | サービスタイプ | 
**service_status** | **str** | サービス状況 * on_trial お試し中 * link_down_on_trial お試し中（一時停止） * in_use 利用中 * link_down 一時停止中 | 
**cpu_cores** | **int** | CPUコア数 | 
**memory_mebibytes** | **int** | メモリ容量(MiB) | 
**storage** | [**List[ServerStorageInner]**](ServerStorageInner.md) | ストレージ情報 | 
**zone** | [**ServerZone**](ServerZone.md) |  | 
**options** | **List[str]** | オプション（追加ソフトウェア） | 
**version** | **str** | プランの世代 | 
**ipv4** | [**ServerIpv4**](ServerIpv4.md) |  | 
**ipv6** | [**ServerIpv6**](ServerIpv6.md) |  | 
**contract** | [**ServerContract**](ServerContract.md) |  | 
**power_status** | **str** | 電源ステータス * power_on 電源ON * in_shutdown シャットダウン中 * power_off 電源OFF * installing OSインストール中 * in_scaleup スケールアップ中 * migration サーバー移行作業中 * unknown 不明（電源状態を取得できない） このエンドポイントが返す電源ステータスはキャッシュされた情報のため、最新の正確な電源ステータスが必要な場合は **サーバーの電源状態を取得する**&#x60;/servers/{server_id}/power-status&#x60;をご利用ください | 

## Example

```python
from sakura_vps_client_py.models.server import Server

# TODO update the JSON string below
json = "{}"
# create an instance of Server from a JSON string
server_instance = Server.from_json(json)
# print the JSON string representation of the object
print(Server.to_json())

# convert the object into a dict
server_dict = server_instance.to_dict()
# create an instance of Server from a dict
server_from_dict = Server.from_dict(server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


