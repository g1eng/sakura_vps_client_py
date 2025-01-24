# ProblemDetails404


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** | エラーの内容 | [optional] 

## Example

```python
from sakura_vps_client_py.models.problem_details404 import ProblemDetails404

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetails404 from a JSON string
problem_details404_instance = ProblemDetails404.from_json(json)
# print the JSON string representation of the object
print(ProblemDetails404.to_json())

# convert the object into a dict
problem_details404_dict = problem_details404_instance.to_dict()
# create an instance of ProblemDetails404 from a dict
problem_details404_from_dict = ProblemDetails404.from_dict(problem_details404_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


