#!/bin/sh

API_VERSION=`jq .info.version < spec/spec.json`
{
  awk "{ gsub(\": 不明\",\": ${API_VERSION:-不明}\"); print }" < README.tpl 
  awk 'NR!=1 { print }' < README.md 
  while read line ; do echo \* "$line"; done < AUTHORS 
  echo
  echo
  echo 'The OpenAPI spec included in the repository is derived from the CC-BY 4.0 licensed part of the [original one](https://manual.sakura.ad.jp/vps/api/api-doc/), authored by [Sakura Internet Inc](https://www.sakura.ad.jp).'
} > README.tmp
mv -v README.tmp README.md
