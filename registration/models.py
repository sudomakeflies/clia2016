#Model structure for SIPSA appengine
from google.appengine.ext import ndb

class Registration(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	email = ndb.StringProperty(required=True)
	pass1 = ndb.StringProperty(required=True)
	title = ndb.StringProperty()
	firstname = ndb.StringProperty(required=True)
	lastname = ndb.StringProperty(required=True)
	gender = ndb.StringProperty()
	birthdate = ndb.StringProperty()
	institution = ndb.StringProperty(required=True)
	ilevel2 = ndb.StringProperty()
	ilevel3 = ndb.StringProperty()
	address = ndb.StringProperty(required=True)
	address2 = ndb.StringProperty()
	city = ndb.StringProperty(required=True)
	country = ndb.StringProperty(required=True)
	phone = ndb.StringProperty()
	phone_mobile = ndb.StringProperty()
	payment = ndb.BooleanProperty()
	courses = ndb.BooleanProperty()

