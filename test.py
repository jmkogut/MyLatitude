#!/usr/bin/env bpython

from latitude import application as app, MainMethod

@MainMethod(__name__)
def test():
    app.run(host=app.config.get('HOST_NAME'),
           debug=app.config.get('DEBUG'))
