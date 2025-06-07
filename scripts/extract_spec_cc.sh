#!/bin/sh -ex

ORIGINAL_SPEC_PATH=${ORIGINAL_SPEC_PATH:-${1:?no source specified}}
: ${2:?no destination specified}

{
  echo '{'
  echo '"openapi":'
  jq .openapi < ${ORIGINAL_SPEC_PATH}
  echo ',"info":'
  jq '.info| del(.license,.termsOfService,.contact,.description)' < ${ORIGINAL_SPEC_PATH}
  echo ',"servers":'
  jq .servers < ${ORIGINAL_SPEC_PATH}
  echo ',"security":'
  jq .security < ${ORIGINAL_SPEC_PATH}
  echo ',"paths":'
  jq .paths < ${ORIGINAL_SPEC_PATH}
  echo ',"components":'
  jq .components < ${ORIGINAL_SPEC_PATH}
  echo '}'
} | jq . | tee ${SPEC_PATH:-$2}
#rm -v ${ORIGINAL_SPEC_PATH}
