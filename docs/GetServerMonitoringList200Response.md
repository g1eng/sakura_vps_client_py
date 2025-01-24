# GetServerMonitoringList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | データ総数 | 
**next** | **str** | 次のページへのURL | 
**previous** | **str** | 前のページへのURL | 
**results** | [**List[ServerMonitoring]**](ServerMonitoring.md) |  | 

## Example

```python
from sakura_vps_client_py.models.get_server_monitoring_list200_response import GetServerMonitoringList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServerMonitoringList200Response from a JSON string
get_server_monitoring_list200_response_instance = GetServerMonitoringList200Response.from_json(json)
# print the JSON string representation of the object
print(GetServerMonitoringList200Response.to_json())

# convert the object into a dict
get_server_monitoring_list200_response_dict = get_server_monitoring_list200_response_instance.to_dict()
# create an instance of GetServerMonitoringList200Response from a dict
get_server_monitoring_list200_response_from_dict = GetServerMonitoringList200Response.from_dict(get_server_monitoring_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


