from flask import Blueprint, render_template, request


auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template('login.html')


@auth.route("/signup")
def signup():
    # return render_template('login.html')
    return "signed up"


@auth.route("/logout")
def logout():
    # return render_template('login.html')
    return "lol"
