#Model structure for SIPSA appengine
from google.appengine.ext import ndb

class Abstract(ndb.Model):
	date = ndb.DateProperty(auto_now_add=True)
	name = ndb.StringProperty()
	email = ndb.StringProperty()
	abstract = ndb.BlobProperty()
	subject = ndb.StringProperty()
	filename = ndb.StringProperty()
	mimetype = ndb.StringProperty()
	accepted = ndb.BooleanProperty()
