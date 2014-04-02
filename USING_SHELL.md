The Interactive Shell
=====================

In the application root, run `python shell.py` or if it's executable
`./shell.py` does just as well.

This drops you in a BPython environment that has the Flask `application`
object loaded, the SQLAlchemy `db` object, and loads of friendly helper
[methods][help] to [test][] the functioning status of your install.

Methods
-------

Here's a quick synopsis of the helper methods I wrote for the shell,
Be sure to offer suggestions.

 - `init_db()` - *dynamically creates the default in-memory SQLite store*
 - `get_js_deps()` *caches the static depencies for browser magic*
 - `install()` - *Runs the various actions needed before the app can run*
 - `get_static_html()` - *Really convenient when you're tweaking the CSS files*

[test]: TESTING.md "TODO: write testing docs"
[help}: #methods "Help methods"
