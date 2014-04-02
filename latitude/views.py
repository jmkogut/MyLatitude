from flask    import request, render_template
from latitude import application as app

@app.route("/")
def splash():
    ''' Setup the index route of the website, and render index.html. '''
    User = { 'nickname': 'Chex' }
    return render_template('index.html', user = User )

@app.route("/update", methods=['POST'] )
def update():
    ''' The uri users will update their locs to. '''
    print '/update POST dump :: %s' % request.form
    return render_template( 'updated.html', dump = request.form)

@app.route("/history/<user>")
def history( user ):
    ''' A page to show the history of where someone has been. '''
    limit_to = user if user else request.args.get( 'user' )
    return render_template( 'history.html', user = limit_to )

@app.route("/map/<user>")
def map( user ):
    ''' A live map view for any specific person. '''
    limit_to = user if user else request.args.get( 'user' )
    return render_template( 'map.html', user = limit_to )
