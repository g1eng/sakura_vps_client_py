# sakura_vps_client_py.ApiKeyApi

All URIs are relative to *https://secure.sakura.ad.jp/vps/api/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_key**](ApiKeyApi.md#delete_api_key) | **DELETE** /api-keys/{api_key_id} | APIキーを削除する
[**delete_role**](ApiKeyApi.md#delete_role) | **DELETE** /roles/{role_id} | ロールを削除する
[**get_api_key**](ApiKeyApi.md#get_api_key) | **GET** /api-keys/{api_key_id} | APIキーを取得する
[**get_api_key_list**](ApiKeyApi.md#get_api_key_list) | **GET** /api-keys | APIキーの一覧を取得する
[**get_permission_list**](ApiKeyApi.md#get_permission_list) | **GET** /permissions | 権限の一覧を取得する
[**get_role**](ApiKeyApi.md#get_role) | **GET** /roles/{role_id} | ロールを取得する
[**get_role_list**](ApiKeyApi.md#get_role_list) | **GET** /roles | ロール一覧を取得する
[**post_api_key**](ApiKeyApi.md#post_api_key) | **POST** /api-keys | APIキーを作成する
[**post_api_key_rotate**](ApiKeyApi.md#post_api_key_rotate) | **POST** /api-keys/{api_key_id}/rotate | APIキーのトークンのローテーションを行う
[**post_role**](ApiKeyApi.md#post_role) | **POST** /roles | ロールを作成する
[**put_api_key**](ApiKeyApi.md#put_api_key) | **PUT** /api-keys/{api_key_id} | APIキーを更新する
[**put_role**](ApiKeyApi.md#put_role) | **PUT** /roles/{role_id} | ロールを更新する


# **delete_api_key**
> delete_api_key(api_key_id)

APIキーを削除する

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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    api_key_id = 56 # int | APIキーID

    try:
        # APIキーを削除する
        api_instance.delete_api_key(api_key_id)
    except Exception as e:
        print("Exception when calling ApiKeyApi->delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**| APIキーID | 

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
**404** | APIキーが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(role_id)

ロールを削除する

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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    role_id = 56 # int | ロールID

    try:
        # ロールを削除する
        api_instance.delete_role(role_id)
    except Exception as e:
        print("Exception when calling ApiKeyApi->delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| ロールID | 

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
**404** | ロールが見つからない |  -  |
**409** | ロールを削除できない状態。紐づいているAPIキーがあるなど。 |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> ApiKey get_api_key(api_key_id)

APIキーを取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.api_key import ApiKey
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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    api_key_id = 56 # int | APIキーID

    try:
        # APIキーを取得する
        api_response = api_instance.get_api_key(api_key_id)
        print("The response of ApiKeyApi->get_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->get_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**| APIキーID | 

### Return type

[**ApiKey**](ApiKey.md)

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
**404** | APIキーが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key_list**
> GetApiKeyList200Response get_api_key_list(order=order, role=role, search=search)

APIキーの一覧を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.get_api_key_list200_response import GetApiKeyList200Response
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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    order = 'order_example' # str | データの並び順。項目名の頭に`-`をつけると降順で取得する   例: * 名称昇順: sort=name * 名称降順: sort=-name (optional)
    role = 56 # int | roleのid。ロールで絞り込む (optional)
    search = 'search_example' # str | 名前から部分一致検索 (optional)

    try:
        # APIキーの一覧を取得する
        api_response = api_instance.get_api_key_list(order=order, role=role, search=search)
        print("The response of ApiKeyApi->get_api_key_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->get_api_key_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| データの並び順。項目名の頭に&#x60;-&#x60;をつけると降順で取得する   例: * 名称昇順: sort&#x3D;name * 名称降順: sort&#x3D;-name | [optional] 
 **role** | **int**| roleのid。ロールで絞り込む | [optional] 
 **search** | **str**| 名前から部分一致検索 | [optional] 

### Return type

[**GetApiKeyList200Response**](GetApiKeyList200Response.md)

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

# **get_permission_list**
> GetPermissionList200Response get_permission_list(category=category, code=code)

権限の一覧を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.get_permission_list200_response import GetPermissionList200Response
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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    category = 'server' # str | カテゴリーで絞り込む (optional)
    code = 'get-server-list,get-server,put-server' # str | コードで絞り込む。カンマ区切りで複数指定可能。 (optional)

    try:
        # 権限の一覧を取得する
        api_response = api_instance.get_permission_list(category=category, code=code)
        print("The response of ApiKeyApi->get_permission_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->get_permission_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| カテゴリーで絞り込む | [optional] 
 **code** | **str**| コードで絞り込む。カンマ区切りで複数指定可能。 | [optional] 

### Return type

[**GetPermissionList200Response**](GetPermissionList200Response.md)

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

# **get_role**
> Role get_role(role_id)

ロールを取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.role import Role
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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    role_id = 56 # int | ロールID

    try:
        # ロールを取得する
        api_response = api_instance.get_role(role_id)
        print("The response of ApiKeyApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->get_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| ロールID | 

### Return type

[**Role**](Role.md)

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
**404** | ロールが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_list**
> GetRoleList200Response get_role_list(order=order, search=search)

ロール一覧を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.get_role_list200_response import GetRoleList200Response
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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    order = 'order_example' # str | データの並び順。項目名の頭に`-`をつけると降順で取得する   例: * 名称昇順: sort=name * 名称降順: sort=-name (optional)
    search = 'search_example' # str | 名前と説明文から部分一致検索 (optional)

    try:
        # ロール一覧を取得する
        api_response = api_instance.get_role_list(order=order, search=search)
        print("The response of ApiKeyApi->get_role_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->get_role_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| データの並び順。項目名の頭に&#x60;-&#x60;をつけると降順で取得する   例: * 名称昇順: sort&#x3D;name * 名称降順: sort&#x3D;-name | [optional] 
 **search** | **str**| 名前と説明文から部分一致検索 | [optional] 

### Return type

[**GetRoleList200Response**](GetRoleList200Response.md)

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

# **post_api_key**
> ApiKey post_api_key(api_key=api_key)

APIキーを作成する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.api_key import ApiKey
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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    api_key = sakura_vps_client_py.ApiKey() # ApiKey |  (optional)

    try:
        # APIキーを作成する
        api_response = api_instance.post_api_key(api_key=api_key)
        print("The response of ApiKeyApi->post_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->post_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | [**ApiKey**](ApiKey.md)|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 成功 |  -  |
**400** | 入力値検証エラー |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**409** | APIキーを作成できない状態。上限を超えているなど。 |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_key_rotate**
> ApiKey post_api_key_rotate(api_key_id)

APIキーのトークンのローテーションを行う

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.api_key import ApiKey
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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    api_key_id = 56 # int | APIキーID

    try:
        # APIキーのトークンのローテーションを行う
        api_response = api_instance.post_api_key_rotate(api_key_id)
        print("The response of ApiKeyApi->post_api_key_rotate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->post_api_key_rotate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**| APIキーID | 

### Return type

[**ApiKey**](ApiKey.md)

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
**404** | APIキーが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_role**
> Role post_role(role=role)

ロールを作成する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.role import Role
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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    role = sakura_vps_client_py.Role() # Role |  (optional)

    try:
        # ロールを作成する
        api_response = api_instance.post_role(role=role)
        print("The response of ApiKeyApi->post_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->post_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | [**Role**](Role.md)|  | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 成功 |  -  |
**400** | 入力値検証エラー |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**409** | ロールを作成できない状態。上限を超えているなど。 |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_key**
> ApiKey put_api_key(api_key_id, api_key=api_key)

APIキーを更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.api_key import ApiKey
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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    api_key_id = 56 # int | APIキーID
    api_key = sakura_vps_client_py.ApiKey() # ApiKey |  (optional)

    try:
        # APIキーを更新する
        api_response = api_instance.put_api_key(api_key_id, api_key=api_key)
        print("The response of ApiKeyApi->put_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->put_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**| APIキーID | 
 **api_key** | [**ApiKey**](ApiKey.md)|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

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
**404** | APIキーが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_role**
> Role put_role(role_id, role=role)

ロールを更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.role import Role
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
    api_instance = sakura_vps_client_py.ApiKeyApi(api_client)
    role_id = 56 # int | ロールID
    role = sakura_vps_client_py.Role() # Role |  (optional)

    try:
        # ロールを更新する
        api_response = api_instance.put_role(role_id, role=role)
        print("The response of ApiKeyApi->put_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->put_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| ロールID | 
 **role** | [**Role**](Role.md)|  | [optional] 

### Return type

[**Role**](Role.md)

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
**404** | ロールが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

