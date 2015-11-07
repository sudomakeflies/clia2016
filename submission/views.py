# -*- encoding:utf-8 -*-
"""views.py"""

from flask import render_template, request, redirect, session, make_response, Response
from submission.models import Abstract
from registration.models import Registration

from google.appengine.ext import db
from google.appengine.ext import ndb

def submission():
    return render_template('submission/submissions.html')

def rules_abstracts():
    return render_template('submission/rules-abstracts.html')

def abstracts():
    if request.method == 'POST':
        try:
            rg = Registration.query()
            rgs = rg.filter(Registration.email==request.form['email'],
                        Registration.pass1==request.form['password']).fetch()[0]
            if rgs:
                session['userinfo'] = rgs.to_dict()
                return redirect("/submissions/submit")
            else:
                return redirect('/registration/?abstracts=true')
        except:
            return redirect('/registration/?abstracts=true')
    else:
        return render_template('submission/login.html')

def submit():
    if request.method == 'POST':
        file = request.files['abstract']
        MAX_IMAGE_SIZE = 1024 * 1024
        if file:
            filestream = file.read()
            if len(filestream) > MAX_IMAGE_SIZE:
                return "Too large abstract size (must be less than 1 MB)"
            else:
                ab = Abstract()
                ab.email = request.form['email']
                ab.name = request.form['name']
                ab.subject = request.form['subject']
                ab.abstract = db.Blob(filestream)
                ab.filename = file.filename
                ab.mimetype = file.mimetype
                ab.put()
                return redirect('/thanks')
        else:
            return "Not file attached"

    else:
        return render_template('submission/abstracts.html')


def service_download(abkey):
    ab = Abstract.get_by_id(int(abkey))
    if ab is not None:
        response = make_response(ab.abstract)
        response.headers['Content-Disposition'] = 'attachment; filename=' + str(ab.filename.replace(" ", "_"))
        response.headers['Content-Type'] = str(ab.mimetype)
        return response
    else:
        return "Blob not found"

subjects = {1:"Agricultural and agro-industrial machinery",
2: "Water and soil engineering",
3:"Postharvest technology and agribusiness",
4:"Rural infrastructure and management environments",
5:"Control and automation in biosystems",
6:"Geoinformatics",
7:"Alternative energy in agriculture",
8:"Sustainable rural development",
9:"Education in agricultural and biosystems engineering"}

import datetime

def to_json(o):
    """
    Custom serializer function
    """
    if isinstance(o, list):
        return [to_json(l) for l in o]
    if isinstance(o, dict):
        x = {}
        for l in o:
            x[l] = to_json(o[l])
        return x
    if isinstance(o, datetime.date):
        return o.isoformat()
    if isinstance(o, ndb.GeoPt):
        return {'lat': o.lat, 'lon': o.lon}
    if isinstance(o, ndb.Key):
        return o.id()
    if isinstance(o, ndb.Model):
        dct = o.to_dict()
        dct['id'] = o.key.id()
        return to_json(dct)
    return o

def service_subject(subject_id):
    ab = Abstract.query()
    qabs = ab.filter(Abstract.subject==subjects[int(subject_id)]).fetch()
    return render_template('submission/get_abstracts_by_subject.html', qabs=qabs, subject=subjects[int(subject_id)])
