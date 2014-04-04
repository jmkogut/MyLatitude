from flask import Blueprint, request, render_template, abort
from latitude.util import log
from simplejson import dumps as JSON

API = Blueprint('api', __name__) #, template_folder='templates')
K,V = 'key', 'value'
_resp = lambda k: lambda v:  {K:k, V:v}

@API.route('/get/<key>')
def read(key):
    return JSON(_resp(key)("default value"))

@API.route('/set/<key>', methods=['GET', 'POST'])
@API.route('/set/<key>/<value>')
def write(key, value=None):
    if request.method == 'GET' and value == None :
        return JSON({
            'error': "You didn't supply a value to set {0} to.".format(key)
        }), 500

    return JSON(_resp(key)(request.form[V] if V in request.form else value))
