#!/bin/sh

API_VERSION=`jq .info.version < spec/spec.json`
awk "{ gsub(\": 不明\",\": ${API_VERSION:-不明}\"); print }" < README.tpl > README.tmp
awk 'NR!=1 { print }' < README.md >> README.tmp
mv -v README.tmp README.md
