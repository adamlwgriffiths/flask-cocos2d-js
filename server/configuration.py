from __future__ import absolute_import, print_function

_configuration = None
def create():
    global _configuration
    _configuration = {}
    return _configuration

def destroy():
    global _configuration
    _configuration =None

def configuration():
    global _configuration
    return _configuration
