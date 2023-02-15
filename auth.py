from flask import Blueprint, render_template, request, flash


auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template('login.html')


@auth.route("/signup", methods=['POST', 'GET'])
def signup():
    # if request.method == 'POST':
    #     email = request.form['email']
    #     username = request.form['username']
    #     password = request.form['password']
    #     confirmPassword = request.form['confirm-password']

    #     if len(password) < 8:
    #         flash("password is short", category="error")

    return render_template('signup.html')


@auth.route("/logout")
def logout():
    # return render_template('login.html')
    return "lol"
