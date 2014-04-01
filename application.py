#!/usr/bin/env python

from flask import *

# The WSGI configuration on Elastic Beanstalk requires
# the callable be named 'application' by default.
application = Flask(__name__)

# Setup the root route of the website, and render the 'index.html' template
@application.route("/")
@application.route("/dash")
def dash():
    user = { 'nickname': 'Chex' }
    return render_template('index.html', user = user )

@application.route("/history")
def history():
    limit = request.args.get('q')

    return render_template('history.html', query = limit )

if __name__ == '__main__':
	application.debug = True
	application.run( host='0.0.0.0' )
