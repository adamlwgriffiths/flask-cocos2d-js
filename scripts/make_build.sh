#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pushd ${DIR}

source vars.sh

cd ..

# check if the build dir exists
if [ ! -d ./${BUILD_DIR} ]; then
    # if not, check if we've got a release repo set
    if [ -n ${RELEASE_REPO} ]; then
        # clone the release repo
        git clone ${RELEASE_REPO} ${BUILD_DIR}
    else
        # just make the directory
        mkdir -p ${BUILD_DIR}
    fi
fi

# remove any existing published work
rm -rf ${BUILD_DIR}/*

# publish the app
pushd ${COCOS_DIR}
node tools/publish.js
popd

# copy cocos build
mkdir -p ${BUILD_DIR}/cocos
cp -r ${COCOS_DIR}/publish/html5/* ${BUILD_DIR}/cocos
# delete the cocos build
rm -rf ${COCOS_DIR}/publish

# copy support files for heroku
cp Procfile requirements.txt ${BUILD_DIR}

# copy scripts
mkdir -p ${BUILD_DIR}/scripts
cp scripts/run_flask.sh.release ${BUILD_DIR}/scripts/run_flask.sh

# copy server
cp server.py ${BUILD_DIR}
cp -r server ${BUILD_DIR}/server

popd
