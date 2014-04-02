Using
=====

_a brief overview of the technologies used in MyLat_

MyLat is hosted on the Amazon Elastic Beanstalk engine. It uses Python 2.7, and Flask for the web framework. The database is saved in memory using python-sqlite3 (default on practically every host) and is occasionally written to fs just in case. ORM is handled by quick_orm / SQLAlchemy, I really despise writing SQL. I'll always do anything I can to avoid it.

This web app was an interesting exercise in patience, Amazon's RDS was incredibly frustrating to use. I ended up saying fuck it and stuck with sqlite.

The map is rendered using OpenStreetMaps, stock theme. I will probably migrate away from it some day but it currently does the trick.
