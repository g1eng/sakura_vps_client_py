# sakura_vps_client_py.DiscApi

All URIs are relative to *https://secure.sakura.ad.jp/vps/api/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_disc_list**](DiscApi.md#get_disc_list) | **GET** /discs | ディスク情報一覧を取得する


# **get_disc_list**
> GetDiscList200Response get_disc_list()

ディスク情報一覧を取得する

追加ソフトウェアのディスク情報です。WindowsのCDドライブにマウントして利用します。

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.get_disc_list200_response import GetDiscList200Response
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
    api_instance = sakura_vps_client_py.DiscApi(api_client)

    try:
        # ディスク情報一覧を取得する
        api_response = api_instance.get_disc_list()
        print("The response of DiscApi->get_disc_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscApi->get_disc_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetDiscList200Response**](GetDiscList200Response.md)

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

