#Model structure for SIPSA appengine
from google.appengine.ext import ndb

class Payment(ndb.Model):
	created = ndb.DateProperty(auto_now_add=True)
	email = ndb.StringProperty(required=True)
	own_name = ndb.StringProperty()
	reference = ndb.StringProperty(required=True)
	name = ndb.StringProperty(required=True)
	description = ndb.StringProperty()
