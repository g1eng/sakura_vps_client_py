# sakura_vps_client_py.ZoneApi

All URIs are relative to *https://secure.sakura.ad.jp/vps/api/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zone_list**](ZoneApi.md#get_zone_list) | **GET** /zones | ゾーン情報一覧を取得する


# **get_zone_list**
> GetZoneList200Response get_zone_list(page=page, per_page=per_page)

ゾーン情報一覧を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.get_zone_list200_response import GetZoneList200Response
from sakura_vps_client_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://secure.sakura.ad.jp/vps/api/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = sakura_vps_client_py.Configuration(
    host = "https://secure.sakura.ad.jp/vps/api/v7"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = sakura_vps_client_py.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sakura_vps_client_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sakura_vps_client_py.ZoneApi(api_client)
    page = 56 # int |  (optional)
    per_page = 10 # int |  (optional) (default to 10)

    try:
        # ゾーン情報一覧を取得する
        api_response = api_instance.get_zone_list(page=page, per_page=per_page)
        print("The response of ZoneApi->get_zone_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneApi->get_zone_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] [default to 10]

### Return type

[**GetZoneList200Response**](GetZoneList200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

