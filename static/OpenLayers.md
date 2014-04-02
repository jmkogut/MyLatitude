OpenLayers
==========

We use [OpenLayers][map] to render the web map. It's fully operational at the latest
version, 3. (A beta still.) This unfortunately means that we won't be loading OpenLayers
3 from a CDN anytime soon.

Inspiration
-----------

I essentially ripped this [example][] from their [site][] to get this working. All
we're doing is rendering a single point on the map. If you [open][example] that link
you'll find references for every file we need, I've linked them for you here.

 - Map CSS: http://ol3js.org/en/master/css/ol.css
 - JQuery (minified): http://code.jquery.com/jquery-1.7.2.min.js
 - Our custom `map,js`: /static/map.js

These three files are downloaded every time you call [deps][].

Dependencies
------------
Since I'm using a beta version you have to manually cache these files using the shell
command [`get_js_deps()`][deps] at least once before running. I'm pretty sure [install][]
calls it though.

to. In the meantime, running get_js_deps() in the MyLatitude [shell][] (TODO: flesh this
all out) or your maps won't work.

[shell]:    ../USING_SHELL.md      "A helpful guide to the MyLatitude shell"
[deps]:     ../USING_SHELL#deps    "TODO: direct link to get_js_deps() docs"
[install]:  ../USING_SHELL#install "TODO: direct link to install() docs"

[git]:     https://github.com/openlayers/ol3 "GitHub project repo"
[example]: http://ol3js.org/en/master/examples/icon.html
	        "Rendering a marker on your map"
