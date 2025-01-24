# ProblemDetails400Errors

入力値に対するエラーを構造化した情報 (code`invalid`の場合のみ) * `non_field_errors` - リクエスト全体に起因した(単一項目でない)エラー内容 * `*` - 対応した入力項目ごとのエラー内容

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_field_errors** | [**List[InvalidParameterDetailInner]**](InvalidParameterDetailInner.md) |  | [optional] 

## Example

```python
from sakura_vps_client_py.models.problem_details400_errors import ProblemDetails400Errors

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetails400Errors from a JSON string
problem_details400_errors_instance = ProblemDetails400Errors.from_json(json)
# print the JSON string representation of the object
print(ProblemDetails400Errors.to_json())

# convert the object into a dict
problem_details400_errors_dict = problem_details400_errors_instance.to_dict()
# create an instance of ProblemDetails400Errors from a dict
problem_details400_errors_from_dict = ProblemDetails400Errors.from_dict(problem_details400_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


