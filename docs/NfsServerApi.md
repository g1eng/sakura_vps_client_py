# sakura_vps_client_py.NfsServerApi

All URIs are relative to *https://secure.sakura.ad.jp/vps/api/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nfs_server**](NfsServerApi.md#get_nfs_server) | **GET** /nfs-servers/{nfs_server_id} | NFS情報を取得する
[**get_nfs_server_interface**](NfsServerApi.md#get_nfs_server_interface) | **GET** /nfs-servers/{nfs_server_id}/interface | NFSのインターフェースを取得する
[**get_nfs_server_list**](NfsServerApi.md#get_nfs_server_list) | **GET** /nfs-servers | NFS情報一覧を取得する
[**get_nfs_server_power_status**](NfsServerApi.md#get_nfs_server_power_status) | **GET** /nfs-servers/{nfs_server_id}/power-status | NFSの電源状態を取得する
[**get_nfs_server_storage**](NfsServerApi.md#get_nfs_server_storage) | **GET** /nfs-servers/{nfs_server_id}/storage | NFSのストレージ容量情報を取得する
[**post_nfs_server_change_ipv4**](NfsServerApi.md#post_nfs_server_change_ipv4) | **POST** /nfs-servers/{nfs_server_id}/change-ipv4 | NFSのipv4を更新する
[**post_nfs_server_force_reboot**](NfsServerApi.md#post_nfs_server_force_reboot) | **POST** /nfs-servers/{nfs_server_id}/force-reboot | NFSを強制再起動する
[**post_nfs_server_power_on**](NfsServerApi.md#post_nfs_server_power_on) | **POST** /nfs-servers/{nfs_server_id}/power-on | NFSを起動する
[**post_nfs_server_shutdown**](NfsServerApi.md#post_nfs_server_shutdown) | **POST** /nfs-servers/{nfs_server_id}/shutdown | NFSをシャットダウンする
[**put_nfs_server**](NfsServerApi.md#put_nfs_server) | **PUT** /nfs-servers/{nfs_server_id} | NFS情報を更新する
[**put_nfs_server_interface**](NfsServerApi.md#put_nfs_server_interface) | **PUT** /nfs-servers/{nfs_server_id}/interface | NFSのインターフェース情報を更新する


# **get_nfs_server**
> NfsServer get_nfs_server(nfs_server_id)

NFS情報を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.nfs_server import NfsServer
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
    api_instance = sakura_vps_client_py.NfsServerApi(api_client)
    nfs_server_id = 56 # int | NFSのID

    try:
        # NFS情報を取得する
        api_response = api_instance.get_nfs_server(nfs_server_id)
        print("The response of NfsServerApi->get_nfs_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NfsServerApi->get_nfs_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_server_id** | **int**| NFSのID | 

### Return type

[**NfsServer**](NfsServer.md)

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
**404** | NFSが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_server_interface**
> NfsServerInterface get_nfs_server_interface(nfs_server_id)

NFSのインターフェースを取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.nfs_server_interface import NfsServerInterface
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
    api_instance = sakura_vps_client_py.NfsServerApi(api_client)
    nfs_server_id = 56 # int | NFSのID

    try:
        # NFSのインターフェースを取得する
        api_response = api_instance.get_nfs_server_interface(nfs_server_id)
        print("The response of NfsServerApi->get_nfs_server_interface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NfsServerApi->get_nfs_server_interface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_server_id** | **int**| NFSのID | 

### Return type

[**NfsServerInterface**](NfsServerInterface.md)

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
**404** | NFSが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_server_list**
> GetNfsServerList200Response get_nfs_server_list(page=page, per_page=per_page, id=id, switch=switch, zone_code=zone_code, sort=sort)

NFS情報一覧を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.get_nfs_server_list200_response import GetNfsServerList200Response
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
    api_instance = sakura_vps_client_py.NfsServerApi(api_client)
    page = 56 # int |  (optional)
    per_page = 10 # int |  (optional) (default to 10)
    id = 'id_example' # str | idで絞り込む。カンマ区切りで100件まで指定可能。 (optional)
    switch = 56 # int | switchのid 対象のスイッチに接続されているサーバーに絞り込む (optional)
    zone_code = 'zone_code_example' # str | ゾーンコードで絞り込む * tk1 東京第1 * tk2 東京第2 * tk3 東京第3 * os1 大阪第1 * os2 大阪第2 * os3 大阪第3 * is1 石狩第1 (optional)
    sort = 'sort_example' # str | データの並び順。項目名の頭に`-`をつけると降順で取得する   例: * サービスコード昇順: sort=service_code * サービスコード降順: sort=-service_code (optional)

    try:
        # NFS情報一覧を取得する
        api_response = api_instance.get_nfs_server_list(page=page, per_page=per_page, id=id, switch=switch, zone_code=zone_code, sort=sort)
        print("The response of NfsServerApi->get_nfs_server_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NfsServerApi->get_nfs_server_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] [default to 10]
 **id** | **str**| idで絞り込む。カンマ区切りで100件まで指定可能。 | [optional] 
 **switch** | **int**| switchのid 対象のスイッチに接続されているサーバーに絞り込む | [optional] 
 **zone_code** | **str**| ゾーンコードで絞り込む * tk1 東京第1 * tk2 東京第2 * tk3 東京第3 * os1 大阪第1 * os2 大阪第2 * os3 大阪第3 * is1 石狩第1 | [optional] 
 **sort** | **str**| データの並び順。項目名の頭に&#x60;-&#x60;をつけると降順で取得する   例: * サービスコード昇順: sort&#x3D;service_code * サービスコード降順: sort&#x3D;-service_code | [optional] 

### Return type

[**GetNfsServerList200Response**](GetNfsServerList200Response.md)

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

# **get_nfs_server_power_status**
> NfsServerPowerStatus get_nfs_server_power_status(nfs_server_id)

NFSの電源状態を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.nfs_server_power_status import NfsServerPowerStatus
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
    api_instance = sakura_vps_client_py.NfsServerApi(api_client)
    nfs_server_id = 56 # int | NFSのID

    try:
        # NFSの電源状態を取得する
        api_response = api_instance.get_nfs_server_power_status(nfs_server_id)
        print("The response of NfsServerApi->get_nfs_server_power_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NfsServerApi->get_nfs_server_power_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_server_id** | **int**| NFSのID | 

### Return type

[**NfsServerPowerStatus**](NfsServerPowerStatus.md)

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
**404** | サーバーが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | 電源状態が取得できない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_server_storage**
> NfsStorageInfo get_nfs_server_storage(nfs_server_id)

NFSのストレージ容量情報を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.nfs_storage_info import NfsStorageInfo
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
    api_instance = sakura_vps_client_py.NfsServerApi(api_client)
    nfs_server_id = 56 # int | NFSのID

    try:
        # NFSのストレージ容量情報を取得する
        api_response = api_instance.get_nfs_server_storage(nfs_server_id)
        print("The response of NfsServerApi->get_nfs_server_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NfsServerApi->get_nfs_server_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_server_id** | **int**| NFSのID | 

### Return type

[**NfsStorageInfo**](NfsStorageInfo.md)

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
**404** | NFSが見つからない |  -  |
**409** | ストレージ容量情報を取得できない状態 |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | 一時的にストレージ容量情報を取得できない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nfs_server_change_ipv4**
> post_nfs_server_change_ipv4(nfs_server_id, post_nfs_server_change_ipv4_request=post_nfs_server_change_ipv4_request)

NFSのipv4を更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.post_nfs_server_change_ipv4_request import PostNfsServerChangeIpv4Request
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
    api_instance = sakura_vps_client_py.NfsServerApi(api_client)
    nfs_server_id = 56 # int | NFSのID
    post_nfs_server_change_ipv4_request = sakura_vps_client_py.PostNfsServerChangeIpv4Request() # PostNfsServerChangeIpv4Request |  (optional)

    try:
        # NFSのipv4を更新する
        api_instance.post_nfs_server_change_ipv4(nfs_server_id, post_nfs_server_change_ipv4_request=post_nfs_server_change_ipv4_request)
    except Exception as e:
        print("Exception when calling NfsServerApi->post_nfs_server_change_ipv4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_server_id** | **int**| NFSのID | 
 **post_nfs_server_change_ipv4_request** | [**PostNfsServerChangeIpv4Request**](PostNfsServerChangeIpv4Request.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ipv4の設定のリクエストの送信を完了 |  -  |
**400** | 入力値検証エラー |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | NFSが見つからない |  -  |
**409** | ipv4の設定が行えない状態にある（すでにipv4の設定中である場合やNFSが起動されていない場合など） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | ipv4の設定のリクエストの送信に失敗した |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nfs_server_force_reboot**
> post_nfs_server_force_reboot(nfs_server_id)

NFSを強制再起動する

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
    api_instance = sakura_vps_client_py.NfsServerApi(api_client)
    nfs_server_id = 56 # int | NFSのID

    try:
        # NFSを強制再起動する
        api_instance.post_nfs_server_force_reboot(nfs_server_id)
    except Exception as e:
        print("Exception when calling NfsServerApi->post_nfs_server_force_reboot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_server_id** | **int**| NFSのID | 

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
**202** | NFS強制再起動コマンドの送信を完了 |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | NFSが見つからない |  -  |
**409** | 再起動リクエストを受け付けない状態にある（設定状況が設定完了になっていない場合など） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | NFS再起動コマンドの送信に失敗した |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nfs_server_power_on**
> post_nfs_server_power_on(nfs_server_id)

NFSを起動する

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
    api_instance = sakura_vps_client_py.NfsServerApi(api_client)
    nfs_server_id = 56 # int | NFSのID

    try:
        # NFSを起動する
        api_instance.post_nfs_server_power_on(nfs_server_id)
    except Exception as e:
        print("Exception when calling NfsServerApi->post_nfs_server_power_on: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_server_id** | **int**| NFSのID | 

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
**202** | NFS起動コマンドの送信を完了 |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | NFSが見つからない |  -  |
**409** | 起動リクエストを受け付けない状態にある（設定状況が設定完了になっていない場合や、既に起動中の場合など） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | NFS起動コマンドの送信に失敗した |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nfs_server_shutdown**
> post_nfs_server_shutdown(nfs_server_id, post_server_shutdown_request=post_server_shutdown_request)

NFSをシャットダウンする

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.post_server_shutdown_request import PostServerShutdownRequest
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
    api_instance = sakura_vps_client_py.NfsServerApi(api_client)
    nfs_server_id = 56 # int | NFSのID
    post_server_shutdown_request = sakura_vps_client_py.PostServerShutdownRequest() # PostServerShutdownRequest |  (optional)

    try:
        # NFSをシャットダウンする
        api_instance.post_nfs_server_shutdown(nfs_server_id, post_server_shutdown_request=post_server_shutdown_request)
    except Exception as e:
        print("Exception when calling NfsServerApi->post_nfs_server_shutdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_server_id** | **int**| NFSのID | 
 **post_server_shutdown_request** | [**PostServerShutdownRequest**](PostServerShutdownRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | NFSシャットダウンコマンドの送信を完了 |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | NFSが見つからない |  -  |
**409** | シャットダウンリクエストを受け付けない状態にある（設定状況が設定完了になっていない場合や、すでにシャットダウンされている場合など） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | NFSシャットダウンコマンドの送信に失敗した |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_nfs_server**
> NfsServer put_nfs_server(nfs_server_id, put_server_request=put_server_request)

NFS情報を更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.nfs_server import NfsServer
from sakura_vps_client_py.models.put_server_request import PutServerRequest
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
    api_instance = sakura_vps_client_py.NfsServerApi(api_client)
    nfs_server_id = 56 # int | NFSのID
    put_server_request = sakura_vps_client_py.PutServerRequest() # PutServerRequest |  (optional)

    try:
        # NFS情報を更新する
        api_response = api_instance.put_nfs_server(nfs_server_id, put_server_request=put_server_request)
        print("The response of NfsServerApi->put_nfs_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NfsServerApi->put_nfs_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_server_id** | **int**| NFSのID | 
 **put_server_request** | [**PutServerRequest**](PutServerRequest.md)|  | [optional] 

### Return type

[**NfsServer**](NfsServer.md)

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
**404** | NFSが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_nfs_server_interface**
> NfsServerInterface put_nfs_server_interface(nfs_server_id, nfs_server_interface=nfs_server_interface)

NFSのインターフェース情報を更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.nfs_server_interface import NfsServerInterface
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
    api_instance = sakura_vps_client_py.NfsServerApi(api_client)
    nfs_server_id = 56 # int | NFSのID
    nfs_server_interface = sakura_vps_client_py.NfsServerInterface() # NfsServerInterface |  (optional)

    try:
        # NFSのインターフェース情報を更新する
        api_response = api_instance.put_nfs_server_interface(nfs_server_id, nfs_server_interface=nfs_server_interface)
        print("The response of NfsServerApi->put_nfs_server_interface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NfsServerApi->put_nfs_server_interface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_server_id** | **int**| NFSのID | 
 **nfs_server_interface** | [**NfsServerInterface**](NfsServerInterface.md)|  | [optional] 

### Return type

[**NfsServerInterface**](NfsServerInterface.md)

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
**404** | NFSが見つからない |  -  |
**409** | 接続が行えない状態（電源がオフになっていない） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | 一時的に接続操作を受け付けない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

