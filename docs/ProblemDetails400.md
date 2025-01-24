# ProblemDetails400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | エラー内容を示す簡潔な識別子 * &#x60;invalid&#x60; - 不正なリクエスト値,リクエスト値が妥当でない * &#x60;parse_error&#x60; - 不正な形式,リクエスト値を読み取ることができない * &#x60;bad_request&#x60; - リクエストの内容に何らかの問題がある | [optional] 
**message** | **str** | エラーの内容 | [optional] 
**errors** | [**ProblemDetails400Errors**](ProblemDetails400Errors.md) |  | [optional] 

## Example

```python
from sakura_vps_client_py.models.problem_details400 import ProblemDetails400

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetails400 from a JSON string
problem_details400_instance = ProblemDetails400.from_json(json)
# print the JSON string representation of the object
print(ProblemDetails400.to_json())

# convert the object into a dict
problem_details400_dict = problem_details400_instance.to_dict()
# create an instance of ProblemDetails400 from a dict
problem_details400_from_dict = ProblemDetails400.from_dict(problem_details400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


