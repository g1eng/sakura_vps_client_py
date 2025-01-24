# ServerMonitoringSettingsHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | 監視方法 | 
**interval_minutes** | **int** | チェック間隔(分) | 
**port** | **int** | ポート番号 | 
**host** | **str** | 監視用HTTPリクエストのHostヘッダ   RFCの定義に基づいて下記の制限をかけています * ラベルは2つ以上必要 * 各ラベルについて   * 利用できる文字     * 半角数字 0～9     * 半角英小文字 a～z     * 半角記号 -   * 両端が-でないこと   * -が2つ以上続かないこと。ただしpunycodeの接頭辞&#x60;xn--&#x60;を除く   * 下記パターン(RFCなどで予約または禁止されているパターン)と一致しないこと     * isatap     * wpad     * example     * example0～example9 * 最後のラベルについて   * 利用できる文字     * 半角英小文字 a～z   * 下記のパターン(RFC予約済みのDNS名)と一致しないこと     * test     * localhost | 
**path** | **str** | 監視対象のパス * 利用できる文字    * 半角数字 0～9   * 半角英字 A～Z、a～z   * 半角記号 _./~%?&#x3D;-&amp; | 
**basic_auth_username** | **str** | ベーシック認証のユーザー名 * 利用できる文字    * 半角数字 0～9   * 半角英字 A～Z、a～z   * 半角記号 _.-+!@ | 
**basic_auth_password** | **str** | ベーシック認証のパスワード * 利用できる文字    * 半角数字 0～9   * 半角英字 A～Z、a～z   * 半角記号 !#$%&amp;()*+,-./:&lt;&#x3D;&gt;?@[]^_&#x60;{|}~ | 
**status** | **int** | 正常と見なすHTTPステータスコード | 
**sni** | **bool** | SNIを設定しているWebサーバか * true SNI設定あり * false SNI設定なし | 

## Example

```python
from sakura_vps_client_py.models.server_monitoring_settings_health_check import ServerMonitoringSettingsHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ServerMonitoringSettingsHealthCheck from a JSON string
server_monitoring_settings_health_check_instance = ServerMonitoringSettingsHealthCheck.from_json(json)
# print the JSON string representation of the object
print(ServerMonitoringSettingsHealthCheck.to_json())

# convert the object into a dict
server_monitoring_settings_health_check_dict = server_monitoring_settings_health_check_instance.to_dict()
# create an instance of ServerMonitoringSettingsHealthCheck from a dict
server_monitoring_settings_health_check_from_dict = ServerMonitoringSettingsHealthCheck.from_dict(server_monitoring_settings_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


