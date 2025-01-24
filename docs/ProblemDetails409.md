# ProblemDetails409


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** | エラーの内容 | [optional] 

## Example

```python
from sakura_vps_client_py.models.problem_details409 import ProblemDetails409

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetails409 from a JSON string
problem_details409_instance = ProblemDetails409.from_json(json)
# print the JSON string representation of the object
print(ProblemDetails409.to_json())

# convert the object into a dict
problem_details409_dict = problem_details409_instance.to_dict()
# create an instance of ProblemDetails409 from a dict
problem_details409_from_dict = ProblemDetails409.from_dict(problem_details409_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


