
from google.appengine.ext import ndb

class User(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	name = ndb.StringProperty()
	email = ndb.StringProperty()
	thumbnail = ndb.StringProperty()
	active = ndb.BooleanProperty()
	authenticated = ndb.BooleanProperty()
	anonymous = ndb.BooleanProperty()

	def is_active(self):
		return self.active

	def is_authenticated(self):
		return self.authenticated

	def is_anonymous(self):
		return self.anonymous

	def get_id(self):
		return self.key.id()
