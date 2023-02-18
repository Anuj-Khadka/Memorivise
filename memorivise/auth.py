from flask import Blueprint, Flask, render_template, request, flash, redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    # if request.method == 'POST':
    #     email = request.form['email']
    #     password = request.form['password']

    #     user = User.query.filter_by(email=email).first()
    #     if user:
    #         if check_password_hash(user.password, password):
    #             return redirect('/')
    #         else:
    #             flash("incorect password", category="error")
    #     else:
    #         flash("")
    return render_template('login.html')


@auth.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirmPassword = request.form['confirm-password']

        # if len(password) < 8:
        #     flash("password is short", category="error")

        new_user = User(email=email, username=username, password=generate_password_hash(password, method="sha256"))
        try:
            db.session.add(new_user)
            db.session.commit()
            # flash('Account created!', category='success')
            return redirect('/revise')
        except:
            return "there was a problem adding the user"
    else:
        return render_template('signup.html')


@auth.route("/logout")
def logout():
    # return render_template('login.html')
    return "lol"
