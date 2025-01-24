# NfsServerContract

契約情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_code** | **int** | プランコード | 
**plan_name** | **str** | プラン名 | 
**service_code** | **str** | サービスコード | 

## Example

```python
from sakura_vps_client_py.models.nfs_server_contract import NfsServerContract

# TODO update the JSON string below
json = "{}"
# create an instance of NfsServerContract from a JSON string
nfs_server_contract_instance = NfsServerContract.from_json(json)
# print the JSON string representation of the object
print(NfsServerContract.to_json())

# convert the object into a dict
nfs_server_contract_dict = nfs_server_contract_instance.to_dict()
# create an instance of NfsServerContract from a dict
nfs_server_contract_from_dict = NfsServerContract.from_dict(nfs_server_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


