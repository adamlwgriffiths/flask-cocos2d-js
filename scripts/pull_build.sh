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

if [ ! -d ${BUILD_DIR} ]; then
    git clone ${RELEASE_REPO} ${BUILD_DIR}
else
    # remove any existing published work
    pushd ${BUILD_DIR}
    git pull origin master
    popd
fi

popd
