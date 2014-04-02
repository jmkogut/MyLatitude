''' Various HTTP request handlers for unexpected events.
    ( Like a missing file.)
'''
from latitude import render_template, application as app

@app.errorhandler(404)
def not_found( *args ):
    message = "I'm sorry it had to happen like this."
    return render_template('404.html', msg=message)
