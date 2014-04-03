MyLatitude
----------
This is an entirely open-source clone of Google's Latitude functionality
that you can self-host. Don't know what any of that means? You may be in
the wrong place.

![scr](http://i.imgur.com/sQVDHCa.png)

Install
-------
In the app root, launch the shell and execute [`install()`](SHELL.md#install).
It will notify you when the procedure has completed.

Server
------
You can [update][1] your location on this site with your android phone quite easily. Just install [Backitude][] on your phone and [configure](#config) it to POST to this application.

> (Note: will not work begind NAT.)

This will allow you to view your mobile device's location at your [dashboard][2].

Config
------

> TODO: write an easy how-to config

[Backitude]:  https://play.google.com/store/apps/details?id=gaugler.backitude 
                "Backitude for Android"
[tude.conf]:  backitude_config.md
                "Configuring your mobile device."
[1]:   http://lat.mydomain.tld/update
                "MyLatitude update URI"
[2]:    http://lat.mydomain.tld/
                "View MyLatitude web"
