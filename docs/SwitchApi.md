# sakura_vps_client_py.SwitchApi

All URIs are relative to *https://secure.sakura.ad.jp/vps/api/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_switch**](SwitchApi.md#delete_switch) | **DELETE** /switches/{switch_id} | スイッチを削除する
[**get_switch**](SwitchApi.md#get_switch) | **GET** /switches/{switch_id} | スイッチ情報を取得する
[**get_switch_list**](SwitchApi.md#get_switch_list) | **GET** /switches | スイッチ情報一覧を取得する
[**post_switch**](SwitchApi.md#post_switch) | **POST** /switches | スイッチを作成する
[**put_switch**](SwitchApi.md#put_switch) | **PUT** /switches/{switch_id} | スイッチ情報を更新する


# **delete_switch**
> delete_switch(switch_id)

スイッチを削除する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
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
    api_instance = sakura_vps_client_py.SwitchApi(api_client)
    switch_id = 56 # int | スイッチID

    try:
        # スイッチを削除する
        api_instance.delete_switch(switch_id)
    except Exception as e:
        print("Exception when calling SwitchApi->delete_switch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switch_id** | **int**| スイッチID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 成功 |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | スイッチが見つからない |  -  |
**409** | 削除が行えない状態（接続が残っている） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_switch**
> Switch get_switch(switch_id)

スイッチ情報を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.switch import Switch
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
    api_instance = sakura_vps_client_py.SwitchApi(api_client)
    switch_id = 56 # int | スイッチID

    try:
        # スイッチ情報を取得する
        api_response = api_instance.get_switch(switch_id)
        print("The response of SwitchApi->get_switch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchApi->get_switch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switch_id** | **int**| スイッチID | 

### Return type

[**Switch**](Switch.md)

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
**404** | スイッチが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_switch_list**
> GetSwitchList200Response get_switch_list(page=page, per_page=per_page, id=id, zone_code=zone_code, interface=interface, sort=sort, search=search)

スイッチ情報一覧を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.get_switch_list200_response import GetSwitchList200Response
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
    api_instance = sakura_vps_client_py.SwitchApi(api_client)
    page = 56 # int |  (optional)
    per_page = 10 # int |  (optional) (default to 10)
    id = 'id_example' # str | idで絞り込む。カンマ区切りで100件まで指定可能。 (optional)
    zone_code = 'zone_code_example' # str | ゾーンコードで絞り込む * tk1 東京第1 * tk2 東京第2 * tk3 東京第3 * os1 大阪第1 * os2 大阪第2 * os3 大阪第3 * is1 石狩第1 (optional)
    interface = 56 # int | interfaceのid 対象のインターフェースに接続されているスイッチに絞り込む (optional)
    sort = 'sort_example' # str | データの並び順。項目名の頭に`-`をつけると降順で取得する   例: * 接続インターフェース数昇順: sort=interfaces_count * 接続インターフェース数降順: sort=-interfaces_count (optional)
    search = 'search_example' # str | 名前と説明文から部分一致検索 (optional)

    try:
        # スイッチ情報一覧を取得する
        api_response = api_instance.get_switch_list(page=page, per_page=per_page, id=id, zone_code=zone_code, interface=interface, sort=sort, search=search)
        print("The response of SwitchApi->get_switch_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchApi->get_switch_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] [default to 10]
 **id** | **str**| idで絞り込む。カンマ区切りで100件まで指定可能。 | [optional] 
 **zone_code** | **str**| ゾーンコードで絞り込む * tk1 東京第1 * tk2 東京第2 * tk3 東京第3 * os1 大阪第1 * os2 大阪第2 * os3 大阪第3 * is1 石狩第1 | [optional] 
 **interface** | **int**| interfaceのid 対象のインターフェースに接続されているスイッチに絞り込む | [optional] 
 **sort** | **str**| データの並び順。項目名の頭に&#x60;-&#x60;をつけると降順で取得する   例: * 接続インターフェース数昇順: sort&#x3D;interfaces_count * 接続インターフェース数降順: sort&#x3D;-interfaces_count | [optional] 
 **search** | **str**| 名前と説明文から部分一致検索 | [optional] 

### Return type

[**GetSwitchList200Response**](GetSwitchList200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |
**400** | 入力値検証エラー |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_switch**
> PostSwitch201Response post_switch(post_switch_request=post_switch_request)

スイッチを作成する

同一ゾーン内で作成可能なスイッチ数は最大20です

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.post_switch201_response import PostSwitch201Response
from sakura_vps_client_py.models.post_switch_request import PostSwitchRequest
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
    api_instance = sakura_vps_client_py.SwitchApi(api_client)
    post_switch_request = sakura_vps_client_py.PostSwitchRequest() # PostSwitchRequest |  (optional)

    try:
        # スイッチを作成する
        api_response = api_instance.post_switch(post_switch_request=post_switch_request)
        print("The response of SwitchApi->post_switch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchApi->post_switch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_switch_request** | [**PostSwitchRequest**](PostSwitchRequest.md)|  | [optional] 

### Return type

[**PostSwitch201Response**](PostSwitch201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 作成完了 |  -  |
**400** | 入力値検証エラー |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**409** | 作成上限に達している |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_switch**
> Switch put_switch(switch_id, switch=switch)

スイッチ情報を更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.switch import Switch
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
    api_instance = sakura_vps_client_py.SwitchApi(api_client)
    switch_id = 56 # int | スイッチID
    switch = sakura_vps_client_py.Switch() # Switch |  (optional)

    try:
        # スイッチ情報を更新する
        api_response = api_instance.put_switch(switch_id, switch=switch)
        print("The response of SwitchApi->put_switch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwitchApi->put_switch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switch_id** | **int**| スイッチID | 
 **switch** | [**Switch**](Switch.md)|  | [optional] 

### Return type

[**Switch**](Switch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |
**400** | 入力値検証エラー |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | スイッチが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

