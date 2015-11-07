#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

es = Blueprint('es', __name__,
                        template_folder='templates')

@es.route('')
def index():
	return render_template('es/index_ES.html')

@es.route('/organizing-committee')
def organizing_committee():
	return render_template('es/organizing-committee_ES.html')

@es.route('/scientific-committee')
def scientific_committee():
	return render_template('es/scientific-committee_ES.html')

@es.route('/registration')
def registration():
	return render_template('es/registration_ES.html')

@es.route('/submissions')
def submissions():
	return render_template('es/submissions_ES.html')

@es.route('/proceedings')
def proceedings():
	return render_template('es/proceedings_ES.html')

@es.route('/pre-conference-courses')
def preconference_courses():
	return render_template('es/preconference-courses_ES.html')

@es.route('/contact')
def contact():
	return render_template('es/contact_ES.html')
	
@es.route('/venue')
def venue():
	return render_template('es/venue_ES.html')	
	
@es.route('/thanks')
def thanks():
	return render_template('es/thanks_ES.html')
