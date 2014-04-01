MyLatitude
==========

A python/flask application that you can host to replace the functionality of Google's now defunct latitude service.

You can update it from [Backitude][] on Android using a POST to [MyLatitude Update][1]. Configuration instructions for Backitude [can be found here][tude.conf], make sure to test them. Support for iOS currently not researched.

This will allow you to view your mobile device's location at [MyLatitude Dashboard][2].

[Backitude]:  https://play.google.com/store/apps/details?id=gaugler.backitude 
                "Backitude for Android"
[tude.conf]:  backitude_config.md
                "Configuring your mobile device."
[1]: http://lat.mydomain.tld/update
                "MyLatitude update URI"
[2]:    http://lat.mydomain.tld/
                "View MyLatitude web"
