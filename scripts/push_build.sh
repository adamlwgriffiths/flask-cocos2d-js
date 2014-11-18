#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pushd ${DIR}

source vars.sh

cd ..

if [ -z ${RELEASE_DEPO} ]; then
    echo "RELEASE_REPO not set"
    return
fi

cd ${BUILD_DIR}
git push orgin master

popd
