from flask import Flask, Blueprint, render_template, request, redirect, flash
from .models import Revise, Contact
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
        return render_template('revise.html', revisions=revisions, user=current_user)


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
        return render_template("update.html", update=update, user=current_user)


@views.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        contactEmail = request.form["contact-email"]
        contactUser = request.form["contact-name"]
        contactMessage = request.form["contact-message"]

        new_message = Contact(contact_email=contactEmail,
                              contact_name=contactUser, contact_message=contactMessage)
        try:
            db.session.add(new_message)
            db.session.commit()
            flash("Thank you for your message. We recieved it!", category="success")
            return redirect("/contact")
        except:
            return "there was an error sending the message."
    return render_template("contact.html", user=current_user)
