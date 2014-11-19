#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pushd ${DIR}

source vars.sh

cd ..

if [ -z ${RELEASE_REPO} ]; then
    echo "RELEASE_REPO not set"
    exit 1
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
