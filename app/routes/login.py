# Python modules
import os 

# Flask modules
from flask import render_template, request, url_for, redirect, send_from_directory
from flask_login import login_user, logout_user

# App modules
from app import app, lm, db
from app.models import Client
from app.forms import LoginForm, RegisterForm

# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return Client.query.get(int(user_id))

# Logout user
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

# Register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    
    # declare the Registration Form
    form = RegisterForm(request.form)

    msg = None
    success = False

    if request.method == 'GET': 

        return render_template( 'accounts/register.html', form=form, msg=msg )

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        first_name = request.form.get('first_name', '', type=str)
        last_name = request.form.get('last_name', '', type=str) 
        email = request.form.get('email', '', type=str) 

        # filter User out of database through username
        user_by_email = Client.query.filter_by(email=email).first()

        if user_by_email:
            msg = 'Error: User exists!'
        
        else:
            user = Client(first_name, last_name, email)

            db.session.add(user)
            db.session.commit()

            msg = 'User created, please <a href="' + url_for('login') + '">login</a>'     
            success = True
    else:
        msg = 'Input error'     

    return render_template( 'accounts/register.html', form=form, msg=msg, success=success )

# Authenticate user
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    # Declare the login form
    form = LoginForm(request.form)

    # Flask message injected into the page, in case of any errors
    msg = None

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        email = request.form.get('email', '', type=str)

        # filter User out of database through username
        user = Client.query.filter_by(email=email).first()

        if user:
            login_user(user)
            return redirect(url_for('index'))
        else:
            msg = "Unknown user"

    return render_template( 'accounts/login.html', form=form, msg=msg )
