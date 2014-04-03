Shell
-----
MyLatitude comes with an interactive environment somewhat similar to Django's shell.


Using
-----
In the app root, run `python shell.py` or if you `chmod +x ./shell.py` then you can
just run it directly. Check that you're in your [virtualenv](README.md#packaging) first.

This drops you in a BPython ([why](#why-bpython)) REPL[?](# "Read, Eval, Print, Loop") that
has a few _real_ handy objects available. Flask `app`, SQLAlchemy `db`, and loads of friendly
[methods](#helpers) to help you interact with the application.


Helpers
-------
Here's a quick synopsis of the helper methods I wrote for the shell...

_Be sure to offer suggestions._

Name | Blurp
--- | ---
`init_db()`         | _Creates the default in-memory SQLite store._ <a id="init-db"></a>
`install()`         | _Prepares the app for running._               <a id="install"></a>
`get_js_deps()`     | _Downloads static dependencies._              <a id="get-js-deps"></a>
`get_static_html()` | _Downloads a copy of your index page._        <a id="get-static-html"></a>


Why BPython
-----------
Frankly, I like it's interface ten times more than IPython, I hope you do too.

[test]:    TESTING.md       "TODO: write testing docs"
[why]:     #why-bpython
