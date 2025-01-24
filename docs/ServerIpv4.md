# ServerIpv4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | アドレス | 
**netmask** | **str** | サブネットマスク | 
**gateway** | **str** | ゲートウェイのアドレス | 
**nameservers** | **List[str]** | ネームサーバーのアドレスリスト | 
**hostname** | **str** | 標準ホスト名 | 
**ptr** | **str** | 逆引きホスト名 | 

## Example

```python
from sakura_vps_client_py.models.server_ipv4 import ServerIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of ServerIpv4 from a JSON string
server_ipv4_instance = ServerIpv4.from_json(json)
# print the JSON string representation of the object
print(ServerIpv4.to_json())

# convert the object into a dict
server_ipv4_dict = server_ipv4_instance.to_dict()
# create an instance of ServerIpv4 from a dict
server_ipv4_from_dict = ServerIpv4.from_dict(server_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


