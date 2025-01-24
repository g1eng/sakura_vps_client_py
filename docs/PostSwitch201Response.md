# PostSwitch201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | [readonly] 
**name** | **str** | 名前 | 
**description** | **str** | 説明 | 
**switch_code** | **str** | スイッチコード | [readonly] 
**zone** | [**PostSwitch201ResponseZone**](PostSwitch201ResponseZone.md) |  | 
**server_interfaces** | **List[int]** | 接続されているサーバーのインターフェースid | [readonly] 
**nfs_server_interfaces** | **List[int]** | 接続されている追加ストレージ（NFS）のインターフェースid | [readonly] 
**external_connection** | **object** | 接続されている外部接続の情報 | [readonly] 

## Example

```python
from sakura_vps_client_py.models.post_switch201_response import PostSwitch201Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostSwitch201Response from a JSON string
post_switch201_response_instance = PostSwitch201Response.from_json(json)
# print the JSON string representation of the object
print(PostSwitch201Response.to_json())

# convert the object into a dict
post_switch201_response_dict = post_switch201_response_instance.to_dict()
# create an instance of PostSwitch201Response from a dict
post_switch201_response_from_dict = PostSwitch201Response.from_dict(post_switch201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


