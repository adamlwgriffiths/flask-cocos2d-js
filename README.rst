================
Flask-Cocos2D-JS
================

A Flask project for hosting Cocos2D projects.


Features
========

* Supports Debug and Released builds.
* Provides scripts for managing builds.
* Includes Procfile for Heroku deployments.


Quick Start
============

::
    
    cd flask-cocos2d-js

    # create a new project in the ./cocos directory, otherwise copy your existing one here
    # be sure to include any hidden files (.cocos-project.json)
    cocos new cocos -l js

    pip install -r requirements.txt

    # run the bash script
    ./scripts/run_debug.sh
    # or run the python script
    python server.py --debug


Adding Release Build Support
============================

Cocos2D doesn't copy the release scripts into the project directory.
They cannot be run from the SDK directory where they are located, they
must be copied.

Cocos uses Node.js for it's build system.

::

    # copy the cocos2d-js tools from the SDK directory
    # use what-ever version of the SDK you need
    cp -r cocos2d-js-v3.1/frameworks/cocos2d-html5/tools cocos/tools

    # make a release build
    ./scripts/make_build.sh

    # run the release build
    ./scripts/run_release.sh

    # run release from inside the release 
    cd build
    ./scripts/run_release.sh
    # or run the python script
    python server.py --release


Dependencies
============

* Cocos2d-JS
* Python
* Flask

Node.js is required For Release Builds.


Authors
=======

* `Adam Griffiths <http://www.github.com/adamlwgriffiths>`_

