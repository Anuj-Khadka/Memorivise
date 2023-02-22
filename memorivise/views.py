from flask import Flask, Blueprint, render_template, request, redirect
from .models import Revise
from . import db
from flask_login import current_user, login_required

views = Blueprint("views", __name__)


@views.route("/")
def index():
    return render_template("index.html", user=current_user)

@views.route("/revise", methods=['POST', 'GET'])
@login_required 
def revise():
    if request.method == 'POST':
        revise_title = request.form['title']
        revise_description = request.form['description']
        new_revise = Revise(title=revise_title, description=revise_description)

        try:
            db.session.add(new_revise)
            db.session.commit()
            return redirect('/revise')
        except:
            return "there was some problem adding the content."

    else:
        revisions = Revise.query.order_by(Revise.date).all()
        return render_template('revise.html', revisions=revisions)


@views.route("/revise/delete/<int:id>")
def delete(id):
    card_to_delete = Revise.query.get(id)

    try:
        db.session.delete(card_to_delete)
        db.session.commit()
        return redirect("/revise")

    except:
        return "there was a problem deleting the card."


@views.route("/revise/update/<int:id>", methods=['POST', 'GET'])
def update(id):
    update = Revise.query.get_or_404(id)

    if request.method == 'POST':
        update.title = request.form['title']
        update.description = request.form['description']

        try:
            db.session.commit()
            return redirect('/revise')

        except:
            return "Sorry! there was a problem updating the card"

    else:
        return render_template("update.html", update=update)


@views.route("/contact")
def contact():
    return "this is a contact page haha"