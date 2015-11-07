# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template

frontend = Blueprint('frontend',__name__)

#Conference
@frontend.route('/')
def index():
	return render_template('index.html')

@frontend.route('/pre-conference-courses')
def preconference_courses():
	return render_template('preconference-courses.html')

# @frontend.route('/registration')
# def registration():
# 	return render_template('registration/index.html')

#app
@frontend.route('/submissions')
def submissions():
	return render_template('submissions.html')

@frontend.route('/proceedings')
def proceedings():
	return render_template('proceedings.html')

#Committees
@frontend.route('/organizing-committee')
def organizing_committee():
	return render_template('organizing-committee.html')

@frontend.route('/scientific-committee')
def scientific_committee():
	return render_template('scientific-committee.html')

#Sponsors
@frontend.route('/sponsors')
def sponsors():
	return render_template('sponsors.html')

#Venue
@frontend.route('/venue')
def venue():
	return render_template('venue.html')

#Contact us
@frontend.route('/contact')
def contact():
	return render_template('contact.html')

@frontend.route('/thanks')
def thanks():
	return render_template('thanks.html')
