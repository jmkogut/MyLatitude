from flask    import request, render_template, session, redirect, url_for
from latitude import application as app, log, google

@app.route("/")
def splash():
    ''' Setup the index route of the website, and render index.html. '''
    return render_template('index.html', user=user )


@app.route("/update", methods=['POST'] )
def update():
    ''' The uri users will update their locs to.

    | - SAMPLE
    | ImmutableMultiDict([('username', u'joshua'), ('dottru@gmail.com',
    | u'dottru@gmail.com'), ('s2', u'device'), ('loc_timestamp', u'25200'),
    | ('longitude', u'-122.23457336425781'), ('offset', u'-07:00'), ('latitude',
    | u'38.08940505981445'), ('password', u'lolhax'), ('req_timestamp', u'1396511928'),
    | ('accuracy', u'0.0')])
    '''
    print '/update POST dump :: %s' % request.form
    return render_template( 'updated.html', dump = request.form)


@app.route("/history/<user>")
def history( user ):
    ''' A page to show the history of where someone has been. '''
    limit_to = user if user else request.args.get( 'user' )
    return render_template( 'history.html', user = limit_to )


@app.route("/login", methods=['GET', 'POST'])
def login():
    ''' Initiates an oauth login, callback is /auth '''
    if 'openid' in session.keys():
        return "Already logged in. {0}" % session['openid'],
    else:
        cb = url_for('oauth', _external=True)
        return log(google.authorize(callback=cb)

@app.route(app.config.get('REDIRECT_URI')) #, methods=['GET', 'POST'])
@google.authorized_handler
def oauth(resp):
    ''' Initiates an oauth login, callback is /oauth '''
    log("OAUTH CALLBACK ARGS   {0}", request.args)
    log("               POST {0}", request.form)
    log("               user   {0}", user)
    log("               openid {0}", openid)
    log("               resp {0}", resp)
    access_token = resp('access_token')
    session['access_token'] = access_token, ''

    # just wherever, index later
    return redirect(url_for('/test/auth'))
    #if g.user:
    #    return "Already logged in. Echoing things {0}".format(g.user)

 @google.tokengetter
 def tokengetter():
    log("access_token")
    return log(session.get('access_token'))


''' TESTING VIE WS ============================
    - Google login:    /test/login
    - Blank map:       /test/map
    - Data:
                       /test/db/counts :: Shows row counts for all models.

'''
@app.route("/test/auth")
def auth():
    ''' Initiates an oauth login, callback is /auth '''
    access_token = session.get('access_token')

    if access_token is None:
        log("Not logged in user can't test auth.")
        return redirect(url_for('login'))



    else:
        log("user {0}", user)
        log("openid {0}", openid)
        from urllib2 import Request, urlopen, URLError

        headers = {'Authorization': 'OAuth '+access_token}
        req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                      None, headers)
        try:
            res = urlopen(req)
        except URLError, e:
            if e.code == 401:
                # Unauthorized - bad token
                Identity.set_expired(access_token)
                session.pop('access_token', None)
                return re
                direct(url_for('login'))
            return res.read()
            # here is where we confirm name
            # Identity.for_token(token=access_token, ...)
        return res.read()


''' DEBUG ONLY MAP TEST ROUTE '''
if app.config.get('DEBUG'):
    @app.route("/test/map")
    def map():
        ''' A view to test map rendering. '''
        return render_template( 'simple_map.html' )
