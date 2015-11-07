#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

pt = Blueprint('pt', __name__,
                        template_folder='templates')

@pt.route('')
def index():
	return render_template('pt/index_PT.html')

@pt.route('/organizing-committee')
def organizing_committee():
	return render_template('pt/organizing-committee_PT.html')

@pt.route('/scientific-committee')
def scientific_committee():
	return render_template('pt/scientific-committee_PT.html')

@pt.route('/registration')
def registration():
	return render_template('pt/registration_PT.html')

@pt.route('/submissions')
def submissions():
	return render_template('pt/submissions_PT.html')

@pt.route('/proceedings')
def proceedings():
	return render_template('pt/proceedings_PT.html')

@pt.route('/pre-conference-courses')
def preconference_courses():
	return render_template('pt/preconference-courses_PT.html')

@pt.route('/contact')
def contact():
	return render_template('pt/contact_PT.html')
	
@pt.route('/venue')
def venue():
	return render_template('pt/venue_PT.html')	
	
@pt.route('/thanks')
def thanks():
	return render_template('pt/thanks_PT.html')

@pt.route('/sponsors')
def sponsors():
	return render_template('sponsors.html')	
