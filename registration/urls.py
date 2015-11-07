from flask import Blueprint
import views

#blueprint
rurls = Blueprint('registration_app',__name__)

rurls.add_url_rule('/', 'registration', views.registration, methods=['GET','POST'])
rurls.add_url_rule('/login', 'login', views.login, methods=['GET','POST'])
rurls.add_url_rule('/profile', 'profile', views.profile, methods=['GET','POST'])
rurls.add_url_rule('/payment', 'payment', views.payment)
rurls.add_url_rule('/dashboard', 'dashboard', views.dashboard)
