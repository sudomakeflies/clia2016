# -*- encoding:utf-8 -*-
from flask import Flask, request, session
from coClia2016App.views.frontend import frontend
from coClia2016App.views.es_views import es
from coClia2016App.views.pt_views import pt
from registration.urls import rurls
from submission.urls import sburls

app = Flask(__name__)
app.register_blueprint(frontend, url_prefix='')
app.register_blueprint(es, url_prefix='/es')
app.register_blueprint(pt, url_prefix='/pt')
app.register_blueprint(rurls, url_prefix='/registration')
app.register_blueprint(sburls, url_prefix='/submissions')

#Admin's
from flask_admin import Admin, base
from submission.models import Abstract
from submission.admin import AdminAbstract
from registration.models import Registration
from registration.admin import AdminRegistration
from payment.models import Payment
from payment.admin import AdminPayment
admin = Admin(app, name='clia2016.co', template_mode='bootstrap3')
admin.add_view(AdminRegistration(Registration))
admin.add_view(AdminAbstract(Abstract))
admin.add_view(AdminPayment(Payment))

#Errors
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

#CSRF
# @app.before_request
# def csrf_protect():
# 	if request.method == "POST":
# 		token = session.pop('_csrf_token', None)
# 		print token, request.form.get('_csrf_token')
# 		if not token or token != request.form.get('_csrf_token'):
# 			return page_not_found(500)

# def some_random_string(length):
#     import random
#     number = '0123456789'
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     id = ''
#     for i in range(0,length,2):
#         id += random.choice(number)
#         id += random.choice(alpha)
#     return id

# def generate_csrf_token():
#     if '_csrf_token' not in session:
#         session['_csrf_token'] = some_random_string(12)
#     return session['_csrf_token']

# app.jinja_env.globals['csrf_token'] = generate_csrf_token
# #Set session key
# app.secret_key = some_random_string(20)
