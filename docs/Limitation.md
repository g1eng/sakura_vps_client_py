# Limitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_performance_limit** | **str** | CPUリソースの制限可否 | [optional] 
**network_bandwidth_limit** | **str** | ネットワーク帯域の制限可否 | [optional] 
**outbound_port_25_blocking** | **str** | OP25Bの可否 | [optional] 
**storage_iops_limit** | **str** | ストレージのIOPSの制限可否 | [optional] 

## Example

```python
from sakura_vps_client_py.models.limitation import Limitation

# TODO update the JSON string below
json = "{}"
# create an instance of Limitation from a JSON string
limitation_instance = Limitation.from_json(json)
# print the JSON string representation of the object
print(Limitation.to_json())

# convert the object into a dict
limitation_dict = limitation_instance.to_dict()
# create an instance of Limitation from a dict
limitation_from_dict = Limitation.from_dict(limitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


