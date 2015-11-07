# -*- encoding:utf-8 -*-
"""views.py"""

from flask import render_template, request, redirect, url_for, session
from registration.models import Registration


# def registration():
#     return render_template('registration/registration.html')

def registration():
    if request.method == 'POST':
        try:
            rg = Registration.query()
            rgs = rg.filter(Registration.email==request.form['email']).fetch()[0]
            if rgs:
                session['userinfo'] = rgs.to_dict()
                return redirect("/registration/dashboard")
            else:
    		    return redirect("/registration/profile?email=" + request.form['email'])
        except:
            return redirect("/registration/profile?email=" + request.form['email'])
    else:
        return render_template('registration/index.html')

def login():
    if request.method == 'POST':
        try:
            rg = Registration.query()
            rgs = rg.filter(Registration.email==request.form['email'],
                            Registration.pass1==request.form['password']).fetch()[0]
            if rgs:
                print "Login success"
                session['userinfo'] = rgs.to_dict()
                return redirect("/registration/dashboard")
                #return render_template('registration/dashboard.html', userinfo=rgs)
        except Exception as e:
            return redirect('/registration/login?info=false')
    else:
        return render_template('registration/login.html')

def profile():
    if request.method == 'POST':
        rg = Registration.query()
        rgs = rg.filter(Registration.email==request.form['email']).fetch()
        if rgs:
            return "Email already registered"
        else:
            r = Registration()
            f = request.form
            for key in f.keys():
                for value in f.getlist(key):
                    print key,":",value.encode('utf-8')
                    setattr(r, key, value.encode('utf-8'))
            r.put()
            sender = "clia2016-1001@appspot.gserviceaccount.com"
            subject = " An account has been created for you in clia2016.co"
            body = "Welcome to CLIA 2016, you can go to http://www.clia2016.co/registration/login, with your email (%s) and password (%s)"%(request.form['email'], request.form['pass1'])
            html = "<img width='200px' src='http://www.clia2016.co/static/img/logos/clia2016.jpg' /> <h1>Welcome to CLIA 2016</h1> <p>You can go to <a href='http://www.clia2016.co/registration/login'>dashboard</a>, with your email (%s) and password (%s)</p>"%(request.form['email'], request.form['pass1'])
            from google.appengine.api import mail
            try:
                message = mail.EmailMessage(sender=sender, subject=subject)
                message.to = request.form['email']
                message.body = body
                message.html = html
                message.send()
                print "Email sending..."
            except:
                print "Error enviando correo"
            return redirect('/registration/payment?profile=success')
    else:
        email = request.args.get("email")
        return render_template('registration/profile.html', email=email)

def payment():
    return render_template('registration/payment.html')

def dashboard():
    return render_template('registration/dashboard.html')
