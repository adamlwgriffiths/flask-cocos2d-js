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

GIT_VERSION=`git rev-parse HEAD`

cd ${BUILD_DIR}

git add .
git commit -a -m 'Build for commit ${GIT_VERSION}'

popd
