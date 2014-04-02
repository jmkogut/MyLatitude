from app import *

@application.route("/")
''' Setup the index route of the website, and render index.html. '''
def index():
    User = { 'nickname': 'Chex' }
    return render_template('index.html', user=User )

@application.route("/update", methods=[ 'GET','POST'] )
def update():
    ''' The uri users will update their locs to. '''
    if request.method == 'POST':
        print '/update POST dump :: %s' % request.form
        return render_template( 'update_done.html', dump=request.form)
    else:
        print "GET /update :: God I'm stupid"
        return render_template( 'update_help.html' )

@application.route("/history/<user>")
def history( user ):
    ''' A page to show the history of where someone has been. '''
    limit_to = user if user else request.args.get( 'user' )
    return render_template('history.html', user=limit_to )

@application.route("/map/<user>")
def map( user ):
    ''' A live map view for any specific person. '''
    limit_to = user if user else request.args.get( 'user' )
    return render_template('map.html', user=limit_to )
