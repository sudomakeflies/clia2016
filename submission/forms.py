from wtforms import Form, TextField, BooleanField, SelectMultipleField, validators
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField

class AbstractForm(Form):
    name = TextField('name', [validators.Length(min=4, max=80)])
    email = TextField('email', [validators.Length(min=4, max=80)])
    accepted = BooleanField('accepted')