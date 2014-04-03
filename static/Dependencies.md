Dependencies
------------
We use OpenLayers to render the web map. It's fully operational at the latest
version, 3. (A beta still.) This unfortunately means that we won't be loading your
dependencies from a CDN for quite a while. There are three files we need to cache
pre-launch.


Credits
-------
I essentially ripped this [example][] from their site to get this working. All
we're doing is rendering a single point on the map. If you [open][example] that link
you'll find that it loads three files. A stylesheet, jquery, openlayers.js, and then the
example-specific code.

 - OpenLayers CSS:    http://ol3js.org/en/master/css/ol.css
 - JQuery (minified): http://code.jquery.com/jquery-1.7.2.min.js
 - OpenLayers.js:     http://todo.find/this
 - Map.js (local):    /static/map.js

The three that need caching are downloaded every time you call [deps][].

Dependencies
------------
Since I'm using a beta version you have to manually cache these files using the shell
command [`get_js_deps()`][deps] at least once before running. I'm pretty sure [install][]
calls it though.

to. In the meantime, running get_js_deps() in the MyLatitude [shell][] (TODO: flesh this
all out) or your maps won't work.

[shell]:    ../SHELL.md#using
[deps]:     ../SHELL.md#get-js-deps
[install]:  ../SHELL.md#install

[git]:     https://github.com/openlayers/ol3 "GitHub project repo"
[example]: http://ol3js.org/en/master/examples/icon.html
	        "Rendering a marker on your map"
