import datetime

from flask_admin.contrib.appengine.view import NdbModelView
from flask_admin.base import AdminIndexView, expose
import flask_wtf
from wtforms.ext.appengine.db import model_form
from google.appengine.ext import ndb

from models import Payment

from auth import access

from flask import redirect, url_for #session,  g, request,

class AdminPayment(NdbModelView):
	@access
	def is_accessible(self):
		pass

	def _handle_view(self, name, **kwargs):
		if not self.is_accessible():
			return redirect(url_for("pauth.login"))

	can_create = True
	can_delete = False
	can_edit = True
	form_base_class = flask_wtf.Form
	page_size = 20
	column_list = ('email', 'own_name', 'created', 'reference', 'name', 'description')
