import datetime

from flask_admin.contrib.appengine.view import NdbModelView
from flask_admin.base import AdminIndexView, expose
import flask_wtf
from wtforms.ext.appengine.db import model_form
from google.appengine.ext import ndb

from models import Registration

from auth import access

from flask import redirect, url_for #session,  g, request,

class AdminRegistration(NdbModelView):
	@access
	def is_accessible(self):
		pass

	def _handle_view(self, name, **kwargs):
		if not self.is_accessible():
			print name, kwargs
			return redirect(url_for("rauth.login"))
	# def create_model(self, form):
	# 	try:
	# 		model = self.model()
	# 		model.email = form.email.raw_data[0]
	# 		model.pass1 = form.pass1.raw_data[0]
	# 		model.title = form.title.raw_data[0]
	# 		model.firstname = form.firstname.raw_data[0]
	# 		model.lastname = form.lastname.raw_data[0]
	# 		model.gender = form.gender.raw_data[0]
	# 		model.birthdate = datetime(form.birthdate.raw_data[0])
	# 		model.institution = form.institution.raw_data[0]
	# 		model.ilevel2 = form.ilevel2.data
	# 		model.ilevel3 = form.ilevel3.data
	# 		model.address = form.address.data
	# 		model.address2 = form.address2.data
	# 		model.city = form.city.data
	# 		model.country = form.country.data
	# 		model.phone = form.phone.data
	# 		model.phone_mobile = form.phone_mobile.data
	# 		model.payment = form.payment.data
	# 		model.put()
	# 		return model
	# 	except Exception as ex:
	# 		if not self.handle_view_exception(ex):
	# 		#flash(gettext('Failed to create record. %(error)s',
	# 		#	error=ex), 'error')
	# 			logging.exception('Failed to create record.')
	# 		return False

	# def update_model(self, form, model):
	# 	try:
	# 		model = self.model()
	# 		model.email = form.email.raw_data[0]
	# 		model.pass1 = form.pass1.raw_data[0]
	# 		model.title = form.title.raw_data[0]
	# 		model.firstname = form.firstname.raw_data[0]
	# 		model.lastname = form.lastname.raw_data[0]
	# 		model.gender = form.gender.raw_data[0]
	# 		model.birthdate = datetime(form.birthdate.raw_data[0])
	# 		model.institution = form.institution.raw_data[0]
	# 		model.ilevel2 = form.ilevel2.data
	# 		model.ilevel3 = form.ilevel3.data
	# 		model.address = form.address.data
	# 		model.address2 = form.address2.data
	# 		model.city = form.city.data
	# 		model.country = form.country.data
	# 		model.phone = form.phone.data
	# 		model.phone_mobile = form.phone_mobile.data
	# 		model.payment = form.payment.data
	# 		model.put()
	# 		return model
	# 	except Exception as ex:
	# 		if not self.handle_view_exception(ex):
	# 			#flash(gettext('Failed to create record. %(error)s',
	# 			#	error=ex), 'error')
	# 			logging.exception('Failed to create record.')
	# 		return False

	can_create = True
	can_edit = True
	can_delete = False
	form_base_class = flask_wtf.Form
	page_size = 20
	column_list = ('email', 'institution', 'created', 'country', 'payment')
