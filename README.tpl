# これは何

さくらのVPS APIをPythonで利用するための非公式クライアントライブラリです。

このライブラリは[上流の仕様書](https://manual.sakura.ad.jp/vps/api/api-doc/)が [CC-BY 4.0国際ライセンス](https://creativecommons.org/licenses/by/4.0/deed.ja)で許諾する部分を切り出して作成した[仕様書](/spec/spec.json)を元に、OpenAPI Generator の Python generator を用いてコード生成を行ったものです。

このライブラリは[さくらインターネット](https://www.sakura.ad.jp)が著作権を有する仕様書(バージョン: 不明)を元として作成されています。

# はじめに

本リポジトリでは、クライアントライブラリの包括的な利用方法のサポートを提供しません。
その代わり、このREADMEの末尾と[docs](/docs)配下に、OpenAPI generatorによって自動生成したドキュメンテーションを掲載します。

python-lsp-server のようなLSPサーバーを用いれば、それぞれの関数の利用方法について有益なサジェストを得ることができるでしょう。VSCodeやEmacs、Sublimeなど、主要なテキストエディタはLSPクライアントをサポートしています。


# ライセンス

MIT


# 利用方法 (自動生成)

