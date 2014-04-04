#!/usr/bin/env bpython
""" Interactive shell for debugging, etc. """

from latitude import application as app, db, MainMethod
from latitude import models
from latitude.util import abort, Install

__import__('os').environ['PYTHONINSPECT'] = 'True'


@MainMethod(__name__)
def BPy_Shell():
    """ TODO: write the helpers you mentioned in SHELL.md. """
    try:
        banner = """
~ MyLatitude interactive shell.

  Scope:
        * app               - Flask instance

        * db                - SQLAlchemy instance
        * models            - SQLAlchemy model definitions

        * db_create()       - Create the database & all tables.
        * db_destroy()      - Destroys the database & all tables. """

        import bpython
        scope = {}
        scope['app'] = app
        scope['db']  = db
        scope['models'] = models

        scope['db_create'] = models.METHODS.Create
        scope['db_drop']   = models.METHODS.Drop

        bpython.embed(locals_=scope, banner=banner)
    except Exception, e:
        abort(msg="Encountered an exception while loading the bpython shell. \
            \n -- \n%s" % e.message)
