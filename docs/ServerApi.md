# sakura_vps_client_py.ServerApi

All URIs are relative to *https://secure.sakura.ad.jp/vps/api/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_server_monitorings**](ServerApi.md#delete_server_monitorings) | **DELETE** /servers/{server_id}/monitorings/{server_monitoring_id} | サーバーのサーバー監視情報を削除する
[**get_server**](ServerApi.md#get_server) | **GET** /servers/{server_id} | サーバー情報を取得する
[**get_server_interface**](ServerApi.md#get_server_interface) | **GET** /servers/{server_id}/interfaces/{interface_id} | サーバーのインターフェース情報を取得する
[**get_server_interface_list**](ServerApi.md#get_server_interface_list) | **GET** /servers/{server_id}/interfaces | サーバーのインターフェース情報一覧を取得する
[**get_server_limitation**](ServerApi.md#get_server_limitation) | **GET** /servers/{server_id}/limitation | サーバーの制限情報を取得する
[**get_server_list**](ServerApi.md#get_server_list) | **GET** /servers | サーバー情報一覧を取得する
[**get_server_monitoring**](ServerApi.md#get_server_monitoring) | **GET** /servers/{server_id}/monitorings/{server_monitoring_id} | サーバーのサーバー監視情報を取得する
[**get_server_monitoring_health**](ServerApi.md#get_server_monitoring_health) | **GET** /servers/{server_id}/monitorings/{server_monitoring_id}/health | サーバー監視の監視状態を取得する
[**get_server_monitoring_list**](ServerApi.md#get_server_monitoring_list) | **GET** /servers/{server_id}/monitorings | サーバーのサーバー監視情報一覧を取得する
[**get_server_power_status**](ServerApi.md#get_server_power_status) | **GET** /servers/{server_id}/power-status | サーバーの電源状態を取得する
[**get_server_video_device**](ServerApi.md#get_server_video_device) | **GET** /servers/{server_id}/video-device | サーバーのビデオデバイスの設定を取得する
[**get_server_vnc_console_keymap**](ServerApi.md#get_server_vnc_console_keymap) | **GET** /servers/{server_id}/vnc-console-keymap | コンパネのVNCコンソールのキーマップ情報を取得する
[**post_server_force_reboot**](ServerApi.md#post_server_force_reboot) | **POST** /servers/{server_id}/force-reboot | サーバーを強制再起動する
[**post_server_monitoring**](ServerApi.md#post_server_monitoring) | **POST** /servers/{server_id}/monitorings | サーバーのサーバー監視を作成する
[**post_server_mount_disc**](ServerApi.md#post_server_mount_disc) | **POST** /servers/{server_id}/mount-disc | サーバーにディスクをマウントする
[**post_server_power_on**](ServerApi.md#post_server_power_on) | **POST** /servers/{server_id}/power-on | サーバーを起動する
[**post_server_shutdown**](ServerApi.md#post_server_shutdown) | **POST** /servers/{server_id}/shutdown | サーバーをシャットダウンする
[**put_server**](ServerApi.md#put_server) | **PUT** /servers/{server_id} | サーバー情報を更新する
[**put_server_interface**](ServerApi.md#put_server_interface) | **PUT** /servers/{server_id}/interfaces/{interface_id} | サーバーのインターフェース情報を更新する
[**put_server_ipv4_ptr**](ServerApi.md#put_server_ipv4_ptr) | **PUT** /servers/{server_id}/ipv4-ptr | サーバーのipv4の逆引きホスト名を更新する
[**put_server_ipv6_ptr**](ServerApi.md#put_server_ipv6_ptr) | **PUT** /servers/{server_id}/ipv6-ptr | サーバーのipv6の逆引きホスト名を更新する
[**put_server_monitoring**](ServerApi.md#put_server_monitoring) | **PUT** /servers/{server_id}/monitorings/{server_monitoring_id} | サーバーのサーバー監視情報を更新する
[**put_server_video_device**](ServerApi.md#put_server_video_device) | **PUT** /servers/{server_id}/video-device | サーバーのビデオデバイスの設定を更新する
[**put_server_vnc_console_keymap**](ServerApi.md#put_server_vnc_console_keymap) | **PUT** /servers/{server_id}/vnc-console-keymap | コンパネのVNCコンソールのキーマップ情報を変更する


# **delete_server_monitorings**
> delete_server_monitorings(server_id, server_monitoring_id)

サーバーのサーバー監視情報を削除する

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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    server_monitoring_id = 56 # int | サーバー監視ID

    try:
        # サーバーのサーバー監視情報を削除する
        api_instance.delete_server_monitorings(server_id, server_monitoring_id)
    except Exception as e:
        print("Exception when calling ServerApi->delete_server_monitorings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **server_monitoring_id** | **int**| サーバー監視ID | 

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
**404** | サーバーまたはサーバー監視が見つからない |  -  |
**409** | サーバー監視を削除できない状態（更新ステータスが更新完了でないなど） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server**
> Server get_server(server_id)

サーバー情報を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.server import Server
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID

    try:
        # サーバー情報を取得する
        api_response = api_instance.get_server(server_id)
        print("The response of ServerApi->get_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 

### Return type

[**Server**](Server.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_interface**
> ServerInterface get_server_interface(server_id, interface_id)

サーバーのインターフェース情報を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.server_interface import ServerInterface
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    interface_id = 56 # int | サーバーインターフェースID

    try:
        # サーバーのインターフェース情報を取得する
        api_response = api_instance.get_server_interface(server_id, interface_id)
        print("The response of ServerApi->get_server_interface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_interface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **interface_id** | **int**| サーバーインターフェースID | 

### Return type

[**ServerInterface**](ServerInterface.md)

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
**404** | インターフェースが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_interface_list**
> GetServerInterfaceList200Response get_server_interface_list(server_id, page=page, per_page=per_page)

サーバーのインターフェース情報一覧を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.get_server_interface_list200_response import GetServerInterfaceList200Response
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    page = 56 # int |  (optional)
    per_page = 10 # int |  (optional) (default to 10)

    try:
        # サーバーのインターフェース情報一覧を取得する
        api_response = api_instance.get_server_interface_list(server_id, page=page, per_page=per_page)
        print("The response of ServerApi->get_server_interface_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_interface_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] [default to 10]

### Return type

[**GetServerInterfaceList200Response**](GetServerInterfaceList200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_limitation**
> Limitation get_server_limitation(server_id)

サーバーの制限情報を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.limitation import Limitation
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID

    try:
        # サーバーの制限情報を取得する
        api_response = api_instance.get_server_limitation(server_id)
        print("The response of ServerApi->get_server_limitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_limitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 

### Return type

[**Limitation**](Limitation.md)

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
**503** | サーバーの制限情報の取得に失敗した |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_list**
> GetServerList200Response get_server_list(page=page, per_page=per_page, id=id, switch=switch, zone_code=zone_code, service_type=service_type, ipv4_address=ipv4_address, monitoring_resource_id=monitoring_resource_id, sort=sort, search=search)

サーバー情報一覧を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.get_server_list200_response import GetServerList200Response
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    page = 56 # int |  (optional)
    per_page = 10 # int |  (optional) (default to 10)
    id = 'id_example' # str | idで絞り込む。カンマ区切りで100件まで指定可能。 (optional)
    switch = 56 # int | switchのid 対象のスイッチに接続されているサーバーに絞り込む (optional)
    zone_code = 'zone_code_example' # str | ゾーンコードで絞り込む * tk1 東京第1 * tk2 東京第2 * tk3 東京第3 * os1 大阪第1 * os2 大阪第2 * os3 大阪第3 * is1 石狩第1 (optional)
    service_type = 'service_type_example' # str | サービスタイプで絞り込む (optional)
    ipv4_address = '192.0.2.0' # str | IPアドレスで絞り込む (optional)
    monitoring_resource_id = 'monitoring_resource_id_example' # str | サーバー監視リソースIDで絞り込む (optional)
    sort = 'sort_example' # str | データの並び順。項目名の頭に`-`をつけると降順で取得する   例: * サービスコード昇順: sort=service_code * サービスコード降順: sort=-service_code (optional)
    search = 'search_example' # str | 名前、説明文、ホスト名、ipv4アドレス、ipv6アドレス、サービスコードから部分一致検索 (optional)

    try:
        # サーバー情報一覧を取得する
        api_response = api_instance.get_server_list(page=page, per_page=per_page, id=id, switch=switch, zone_code=zone_code, service_type=service_type, ipv4_address=ipv4_address, monitoring_resource_id=monitoring_resource_id, sort=sort, search=search)
        print("The response of ServerApi->get_server_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] [default to 10]
 **id** | **str**| idで絞り込む。カンマ区切りで100件まで指定可能。 | [optional] 
 **switch** | **int**| switchのid 対象のスイッチに接続されているサーバーに絞り込む | [optional] 
 **zone_code** | **str**| ゾーンコードで絞り込む * tk1 東京第1 * tk2 東京第2 * tk3 東京第3 * os1 大阪第1 * os2 大阪第2 * os3 大阪第3 * is1 石狩第1 | [optional] 
 **service_type** | **str**| サービスタイプで絞り込む | [optional] 
 **ipv4_address** | **str**| IPアドレスで絞り込む | [optional] 
 **monitoring_resource_id** | **str**| サーバー監視リソースIDで絞り込む | [optional] 
 **sort** | **str**| データの並び順。項目名の頭に&#x60;-&#x60;をつけると降順で取得する   例: * サービスコード昇順: sort&#x3D;service_code * サービスコード降順: sort&#x3D;-service_code | [optional] 
 **search** | **str**| 名前、説明文、ホスト名、ipv4アドレス、ipv6アドレス、サービスコードから部分一致検索 | [optional] 

### Return type

[**GetServerList200Response**](GetServerList200Response.md)

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

# **get_server_monitoring**
> ServerMonitoring get_server_monitoring(server_id, server_monitoring_id, page=page, per_page=per_page)

サーバーのサーバー監視情報を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.server_monitoring import ServerMonitoring
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    server_monitoring_id = 56 # int | サーバー監視ID
    page = 56 # int |  (optional)
    per_page = 10 # int |  (optional) (default to 10)

    try:
        # サーバーのサーバー監視情報を取得する
        api_response = api_instance.get_server_monitoring(server_id, server_monitoring_id, page=page, per_page=per_page)
        print("The response of ServerApi->get_server_monitoring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_monitoring: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **server_monitoring_id** | **int**| サーバー監視ID | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] [default to 10]

### Return type

[**ServerMonitoring**](ServerMonitoring.md)

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
**404** | サーバーまたはサーバー監視が見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_monitoring_health**
> ServerMonitoringHealth get_server_monitoring_health(server_id, server_monitoring_id)

サーバー監視の監視状態を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.server_monitoring_health import ServerMonitoringHealth
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    server_monitoring_id = 56 # int | サーバー監視ID

    try:
        # サーバー監視の監視状態を取得する
        api_response = api_instance.get_server_monitoring_health(server_id, server_monitoring_id)
        print("The response of ServerApi->get_server_monitoring_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_monitoring_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **server_monitoring_id** | **int**| サーバー監視ID | 

### Return type

[**ServerMonitoringHealth**](ServerMonitoringHealth.md)

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
**404** | サーバーまたはサーバー監視が見つからない |  -  |
**409** | 監視状態を取得できない状態（更新ステータスが更新完了でないなど） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_monitoring_list**
> GetServerMonitoringList200Response get_server_monitoring_list(server_id, page=page, per_page=per_page, monitoring_resource_id=monitoring_resource_id)

サーバーのサーバー監視情報一覧を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.get_server_monitoring_list200_response import GetServerMonitoringList200Response
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    page = 56 # int |  (optional)
    per_page = 10 # int |  (optional) (default to 10)
    monitoring_resource_id = 'monitoring_resource_id_example' # str | サーバー監視リソースIDで絞り込む (optional)

    try:
        # サーバーのサーバー監視情報一覧を取得する
        api_response = api_instance.get_server_monitoring_list(server_id, page=page, per_page=per_page, monitoring_resource_id=monitoring_resource_id)
        print("The response of ServerApi->get_server_monitoring_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_monitoring_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] [default to 10]
 **monitoring_resource_id** | **str**| サーバー監視リソースIDで絞り込む | [optional] 

### Return type

[**GetServerMonitoringList200Response**](GetServerMonitoringList200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_power_status**
> ServerPowerStatus get_server_power_status(server_id)

サーバーの電源状態を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.server_power_status import ServerPowerStatus
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID

    try:
        # サーバーの電源状態を取得する
        api_response = api_instance.get_server_power_status(server_id)
        print("The response of ServerApi->get_server_power_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_power_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 

### Return type

[**ServerPowerStatus**](ServerPowerStatus.md)

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
**503** | ホストから電源状態が取得できない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_video_device**
> GetServerVideoDevice200Response get_server_video_device(server_id)

サーバーのビデオデバイスの設定を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.get_server_video_device200_response import GetServerVideoDevice200Response
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID

    try:
        # サーバーのビデオデバイスの設定を取得する
        api_response = api_instance.get_server_video_device(server_id)
        print("The response of ServerApi->get_server_video_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_video_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 

### Return type

[**GetServerVideoDevice200Response**](GetServerVideoDevice200Response.md)

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
**503** | ビデオデバイス情報の取得に失敗した |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_vnc_console_keymap**
> Keymap get_server_vnc_console_keymap(server_id)

コンパネのVNCコンソールのキーマップ情報を取得する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.keymap import Keymap
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID

    try:
        # コンパネのVNCコンソールのキーマップ情報を取得する
        api_response = api_instance.get_server_vnc_console_keymap(server_id)
        print("The response of ServerApi->get_server_vnc_console_keymap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_vnc_console_keymap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 

### Return type

[**Keymap**](Keymap.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 取得完了 |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | サーバーが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_server_force_reboot**
> post_server_force_reboot(server_id)

サーバーを強制再起動する

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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID

    try:
        # サーバーを強制再起動する
        api_instance.post_server_force_reboot(server_id)
    except Exception as e:
        print("Exception when calling ServerApi->post_server_force_reboot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 

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
**202** | 強制再起動コマンドの送信を完了 |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | サーバーが見つからない |  -  |
**409** | 電源操作が行えない状態（スケールアップ中など） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | ホストが電源操作を受け付けない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_server_monitoring**
> ServerMonitoring post_server_monitoring(server_id, server_monitoring=server_monitoring)

サーバーのサーバー監視を作成する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.server_monitoring import ServerMonitoring
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    server_monitoring = sakura_vps_client_py.ServerMonitoring() # ServerMonitoring |  (optional)

    try:
        # サーバーのサーバー監視を作成する
        api_response = api_instance.post_server_monitoring(server_id, server_monitoring=server_monitoring)
        print("The response of ServerApi->post_server_monitoring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->post_server_monitoring: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **server_monitoring** | [**ServerMonitoring**](ServerMonitoring.md)|  | [optional] 

### Return type

[**ServerMonitoring**](ServerMonitoring.md)

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
**404** | サーバーが見つからない |  -  |
**409** | サーバー監視を作成できない状態（作成上限数超過など） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_server_mount_disc**
> post_server_mount_disc(server_id, post_server_mount_disc_request=post_server_mount_disc_request)

サーバーにディスクをマウントする

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.post_server_mount_disc_request import PostServerMountDiscRequest
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    post_server_mount_disc_request = sakura_vps_client_py.PostServerMountDiscRequest() # PostServerMountDiscRequest |  (optional)

    try:
        # サーバーにディスクをマウントする
        api_instance.post_server_mount_disc(server_id, post_server_mount_disc_request=post_server_mount_disc_request)
    except Exception as e:
        print("Exception when calling ServerApi->post_server_mount_disc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **post_server_mount_disc_request** | [**PostServerMountDiscRequest**](PostServerMountDiscRequest.md)|  | [optional] 

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
**200** | マウント完了 |  -  |
**400** | 入力値検証エラー |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | サーバーが見つからない |  -  |
**409** | ディスク操作が行えない状態（電源がOFFなど） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | ホストがディスク操作を受け付けない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_server_power_on**
> post_server_power_on(server_id)

サーバーを起動する

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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID

    try:
        # サーバーを起動する
        api_instance.post_server_power_on(server_id)
    except Exception as e:
        print("Exception when calling ServerApi->post_server_power_on: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 

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
**202** | サーバー起動コマンドの送信を完了 |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | サーバーが見つからない |  -  |
**409** | 電源操作が行えない状態（スケールアップ中など） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | ホストが電源操作を受け付けない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_server_shutdown**
> post_server_shutdown(server_id, post_server_shutdown_request=post_server_shutdown_request)

サーバーをシャットダウンする

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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    post_server_shutdown_request = sakura_vps_client_py.PostServerShutdownRequest() # PostServerShutdownRequest |  (optional)

    try:
        # サーバーをシャットダウンする
        api_instance.post_server_shutdown(server_id, post_server_shutdown_request=post_server_shutdown_request)
    except Exception as e:
        print("Exception when calling ServerApi->post_server_shutdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
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
**202** | シャットダウンコマンドの送信を完了 |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | サーバーが見つからない |  -  |
**409** | 電源操作が行えない状態（スケールアップ中など） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | ホストが電源操作を受け付けない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_server**
> Server put_server(server_id, put_server_request=put_server_request)

サーバー情報を更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.put_server_request import PutServerRequest
from sakura_vps_client_py.models.server import Server
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    put_server_request = sakura_vps_client_py.PutServerRequest() # PutServerRequest |  (optional)

    try:
        # サーバー情報を更新する
        api_response = api_instance.put_server(server_id, put_server_request=put_server_request)
        print("The response of ServerApi->put_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->put_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **put_server_request** | [**PutServerRequest**](PutServerRequest.md)|  | [optional] 

### Return type

[**Server**](Server.md)

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
**404** | サーバーが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_server_interface**
> ServerInterface put_server_interface(server_id, interface_id, server_interface=server_interface)

サーバーのインターフェース情報を更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.server_interface import ServerInterface
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    interface_id = 56 # int | サーバーインターフェースID
    server_interface = sakura_vps_client_py.ServerInterface() # ServerInterface |  (optional)

    try:
        # サーバーのインターフェース情報を更新する
        api_response = api_instance.put_server_interface(server_id, interface_id, server_interface=server_interface)
        print("The response of ServerApi->put_server_interface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->put_server_interface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **interface_id** | **int**| サーバーインターフェースID | 
 **server_interface** | [**ServerInterface**](ServerInterface.md)|  | [optional] 

### Return type

[**ServerInterface**](ServerInterface.md)

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
**404** | インターフェースが見つからない |  -  |
**409** | 接続が行えない状態 |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | 一時的に接続操作を受け付けない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_server_ipv4_ptr**
> PutServerIpv4Ptr200Response put_server_ipv4_ptr(server_id, put_server_ipv4_ptr_request=put_server_ipv4_ptr_request)

サーバーのipv4の逆引きホスト名を更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.put_server_ipv4_ptr200_response import PutServerIpv4Ptr200Response
from sakura_vps_client_py.models.put_server_ipv4_ptr_request import PutServerIpv4PtrRequest
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    put_server_ipv4_ptr_request = sakura_vps_client_py.PutServerIpv4PtrRequest() # PutServerIpv4PtrRequest |  (optional)

    try:
        # サーバーのipv4の逆引きホスト名を更新する
        api_response = api_instance.put_server_ipv4_ptr(server_id, put_server_ipv4_ptr_request=put_server_ipv4_ptr_request)
        print("The response of ServerApi->put_server_ipv4_ptr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->put_server_ipv4_ptr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **put_server_ipv4_ptr_request** | [**PutServerIpv4PtrRequest**](PutServerIpv4PtrRequest.md)|  | [optional] 

### Return type

[**PutServerIpv4Ptr200Response**](PutServerIpv4Ptr200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 設定完了 |  -  |
**400** | 入力値検証エラー |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | サーバーが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | DNSの情報取得または設定に失敗した |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_server_ipv6_ptr**
> PutServerIpv4Ptr200Response put_server_ipv6_ptr(server_id, put_server_ipv4_ptr_request=put_server_ipv4_ptr_request)

サーバーのipv6の逆引きホスト名を更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.put_server_ipv4_ptr200_response import PutServerIpv4Ptr200Response
from sakura_vps_client_py.models.put_server_ipv4_ptr_request import PutServerIpv4PtrRequest
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    put_server_ipv4_ptr_request = sakura_vps_client_py.PutServerIpv4PtrRequest() # PutServerIpv4PtrRequest |  (optional)

    try:
        # サーバーのipv6の逆引きホスト名を更新する
        api_response = api_instance.put_server_ipv6_ptr(server_id, put_server_ipv4_ptr_request=put_server_ipv4_ptr_request)
        print("The response of ServerApi->put_server_ipv6_ptr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->put_server_ipv6_ptr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **put_server_ipv4_ptr_request** | [**PutServerIpv4PtrRequest**](PutServerIpv4PtrRequest.md)|  | [optional] 

### Return type

[**PutServerIpv4Ptr200Response**](PutServerIpv4Ptr200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 設定完了 |  -  |
**400** | 入力値検証エラー |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | サーバーが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | DNSの情報取得または設定に失敗した |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_server_monitoring**
> ServerMonitoring put_server_monitoring(server_id, server_monitoring_id, server_monitoring=server_monitoring)

サーバーのサーバー監視情報を更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.server_monitoring import ServerMonitoring
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    server_monitoring_id = 56 # int | サーバー監視ID
    server_monitoring = sakura_vps_client_py.ServerMonitoring() # ServerMonitoring |  (optional)

    try:
        # サーバーのサーバー監視情報を更新する
        api_response = api_instance.put_server_monitoring(server_id, server_monitoring_id, server_monitoring=server_monitoring)
        print("The response of ServerApi->put_server_monitoring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->put_server_monitoring: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **server_monitoring_id** | **int**| サーバー監視ID | 
 **server_monitoring** | [**ServerMonitoring**](ServerMonitoring.md)|  | [optional] 

### Return type

[**ServerMonitoring**](ServerMonitoring.md)

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
**404** | サーバーが見つからない |  -  |
**409** | サーバー監視を更新できない状態（更新ステータスが更新完了でないなど） |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_server_video_device**
> PutServerVideoDeviceRequest put_server_video_device(server_id, put_server_video_device_request=put_server_video_device_request)

サーバーのビデオデバイスの設定を更新する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.put_server_video_device_request import PutServerVideoDeviceRequest
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    put_server_video_device_request = sakura_vps_client_py.PutServerVideoDeviceRequest() # PutServerVideoDeviceRequest |  (optional)

    try:
        # サーバーのビデオデバイスの設定を更新する
        api_response = api_instance.put_server_video_device(server_id, put_server_video_device_request=put_server_video_device_request)
        print("The response of ServerApi->put_server_video_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->put_server_video_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **put_server_video_device_request** | [**PutServerVideoDeviceRequest**](PutServerVideoDeviceRequest.md)|  | [optional] 

### Return type

[**PutServerVideoDeviceRequest**](PutServerVideoDeviceRequest.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功。サーバーの再起動をすることで設定が反映される |  -  |
**400** | 入力値検証エラー |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | サーバーが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | ビデオデバイス情報の設定に失敗した |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_server_vnc_console_keymap**
> Keymap put_server_vnc_console_keymap(server_id, keymap=keymap)

コンパネのVNCコンソールのキーマップ情報を変更する

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sakura_vps_client_py
from sakura_vps_client_py.models.keymap import Keymap
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
    api_instance = sakura_vps_client_py.ServerApi(api_client)
    server_id = 56 # int | サーバーID
    keymap = sakura_vps_client_py.Keymap() # Keymap |  (optional)

    try:
        # コンパネのVNCコンソールのキーマップ情報を変更する
        api_response = api_instance.put_server_vnc_console_keymap(server_id, keymap=keymap)
        print("The response of ServerApi->put_server_vnc_console_keymap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->put_server_vnc_console_keymap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| サーバーID | 
 **keymap** | [**Keymap**](Keymap.md)|  | [optional] 

### Return type

[**Keymap**](Keymap.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功。サーバーの再起動をすることで設定が反映される |  -  |
**400** | 入力値検証エラー |  -  |
**401** | 未ログイン |  -  |
**403** | 権限がない |  -  |
**404** | サーバーが見つからない |  -  |
**429** | リクエスト可能数に達している |  * Retry-After - リクエストが可能になるまでの秒数 <br>  |
**503** | ホストがキーマップ操作を受け付けない |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

