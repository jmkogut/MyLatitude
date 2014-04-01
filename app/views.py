from site import application

# Setup the root route of the website, and render the 'index.html' template
@application.route("/")
@application.route("/dash")
def dash():
    user = { 'nickname': 'Chex' }
    return render_template('index.html', user = user )

@application.route("/update", methods=[ 'GET','POST'] )
def update():

    if request.method == 'POST':
        print '/update POST dump :: %s' % request.form
        return render_template( 'update_done.html', dump=request.form)
    else:
        print "GET /update :: God I'm stupid"
        return render_template( 'update_help.html' )

@application.route("/history/<user>")
def history( user ):
    limit_to = user if user else request.args.get( 'user' )
    return render_template('history.html', user = limit_to )
