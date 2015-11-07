from flask_admin.contrib.appengine.view import NdbModelView
from flask_admin.base import AdminIndexView, expose
import flask_wtf
from wtforms.ext.appengine.db import model_form
from google.appengine.ext import ndb

from jinja2 import Markup

from models import Abstract
from submission.forms import AbstractForm

from auth import access

from flask import redirect, url_for #session,  g, request,

class AdminAbstract(NdbModelView):
    @access
    def is_accessible(self):
        pass

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("rauth.login"))

    can_create = False
    can_delete = False
    form_base_class = flask_wtf.Form
    page_size = 100
    form = AbstractForm
    column_list = ('name', 'email', 'subject', 'date','download', 'accepted')
    column_searchable_list = ('name', 'subject',)
    column_formatters = dict(download=lambda v, c, m, p: Markup('<a href="/submissions/download/%s" >download</a>'%m.key.id()))