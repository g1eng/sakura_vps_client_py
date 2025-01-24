# ProblemDetails429


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** | エラーの内容 | [optional] 

## Example

```python
from sakura_vps_client_py.models.problem_details429 import ProblemDetails429

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetails429 from a JSON string
problem_details429_instance = ProblemDetails429.from_json(json)
# print the JSON string representation of the object
print(ProblemDetails429.to_json())

# convert the object into a dict
problem_details429_dict = problem_details429_instance.to_dict()
# create an instance of ProblemDetails429 from a dict
problem_details429_from_dict = ProblemDetails429.from_dict(problem_details429_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


