#!/bin/sh -ex

ORIGINAL_SPEC_PATH=${ORIGINAL_SPEC_PATH:-spec/openapi.json}

{
  echo '{'
  echo '"openapi":'
  jq .openapi < ${ORIGINAL_SPEC_PATH}
  echo ',"info":'
  jq '.info| del(.license,.termsOfService,.contact,.description)' < ${ORIGINAL_SPEC_PATH} | tr -d \\\n | awk '{ gsub("}$",""); print}'
  echo ',"description": "Sakura VPS API client written in Python (generated with openapi-generator)"}'
  echo ',"servers":'
  jq .servers < ${ORIGINAL_SPEC_PATH}
  echo ',"security":'
  jq .security < ${ORIGINAL_SPEC_PATH}
  echo ',"paths":'
  jq .paths < ${ORIGINAL_SPEC_PATH}
  echo ',"components":'
  jq .components < ${ORIGINAL_SPEC_PATH}
  echo '}'
} | jq . | tee ${SPEC_PATH:-spec/spec.json}
rm -v ${ORIGINAL_SPEC_PATH}
