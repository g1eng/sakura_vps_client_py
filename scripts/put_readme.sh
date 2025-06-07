#!/bin/sh

API_VERSION=`jq .info.version < spec/spec.json`
cp README.md README.md.swp
{
  awk -v version=": ${API_VERSION:-不明}"  '{ gsub(": 不明",version); print }' < README.tpl 
  cat README.md.swp
  echo 'Nomura Suzume <ＳＵＺＵＭe[att]ｅa.g1e.org>

## 本リポジトリのコード生成の再現方法について

Makefileに記載のopenapi-generatorのバージョンがご自身のマシンに導入されていることをご確認の上、`make renew`を実行してください。


## Credit

The OpenAPI spec included in the repository is derived from the CC-BY 4.0 licensed part of the [original one](https://manual.sakura.ad.jp/vps/api/api-doc/), authored by [Sakura Internet Inc](https://www.sakura.ad.jp).
'

} > README.tmp
mv -v README.tmp README.md
