#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pushd ${DIR}
cd ..

cd ${COCOS_DIR}
cocos run -p web --host 0.0.0.0

popd
