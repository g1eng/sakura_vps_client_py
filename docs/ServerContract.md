# ServerContract

契約情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_code** | **int** | プランコード | 
**plan_name** | **str** | プラン名 | 
**service_code** | **str** | サービスコード | 

## Example

```python
from sakura_vps_client_py.models.server_contract import ServerContract

# TODO update the JSON string below
json = "{}"
# create an instance of ServerContract from a JSON string
server_contract_instance = ServerContract.from_json(json)
# print the JSON string representation of the object
print(ServerContract.to_json())

# convert the object into a dict
server_contract_dict = server_contract_instance.to_dict()
# create an instance of ServerContract from a dict
server_contract_from_dict = ServerContract.from_dict(server_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


