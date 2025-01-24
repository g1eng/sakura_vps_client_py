# ServerIpv6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | アドレス | 
**prefixlen** | **int** | プレフィックス長 | 
**gateway** | **str** | ゲートウェイのアドレス | 
**nameservers** | **List[str]** | ネームサーバーのアドレスリスト | 
**hostname** | **str** | 標準ホスト名 | 
**ptr** | **str** | 逆引きホスト名 | 

## Example

```python
from sakura_vps_client_py.models.server_ipv6 import ServerIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of ServerIpv6 from a JSON string
server_ipv6_instance = ServerIpv6.from_json(json)
# print the JSON string representation of the object
print(ServerIpv6.to_json())

# convert the object into a dict
server_ipv6_dict = server_ipv6_instance.to_dict()
# create an instance of ServerIpv6 from a dict
server_ipv6_from_dict = ServerIpv6.from_dict(server_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


