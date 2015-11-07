#google oauth2 for jobs
from flask import session, Blueprint, redirect, request, flash, g, url_for
from flask_oauthlib.client import OAuth

from coClia2016App.models import User
from coClia2016App import app

from settings import ADMIN_EMAILS

urlservice = "/admin/abstrac"#service for the authorized redirect
GOOGLE_ID = '814454990575-n4mlmcfsoicvcjo8n23qvestgvpqqrde.apps.googleusercontent.com'
GOOGLE_SECRET = '25AtPKeZCMQnh2IzPBekPh5O'

sauth = Blueprint('sauth',__name__)
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key=GOOGLE_ID,
    consumer_secret=GOOGLE_SECRET,
    request_token_params={
        'scope': 'https://www.googleapis.com/auth/userinfo.email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@sauth.route('/login')
def login():
    return google.authorize(callback=url_for('sauth.authorized', _external=True))

@sauth.route('/login/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    #app.config['userdata'] = me.data
    user = User.query(User.email == me.data['email']).fetch()
    if not user:
        user = User()
        user.name = me.data['name']
        user.email = me.data['email']
        user.thumbnail = me.data['picture']
        user.active = True
        user.authenticated = True
        user.anonymous = True
        user.active = True
        user.put()
    session['user_id'] = me.data['email']
    session['_fresh'] = True
    flash('Logged in successfully.')
    return redirect(urlservice)


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

def access(f):
    def wrapper(*args, **kwargs):
        if 'google_token' in session:
            me = google.get('userinfo')
            try:
                #if me.data['email'].split("@")[1] == "ingeniagro.org":
                if me.data['email'] in ADMIN_EMAILS:
                    return True
                else:
                    return False
            except:
                return False
        else:
            return False
    return wrapper

app.register_blueprint(sauth, url_prefix='/sauth')
