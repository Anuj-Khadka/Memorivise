from flask import Flask, Blueprint, render_template, request, redirect, jsonify
from .models import Revise
from .speech import transcribe
from .models import Memorivise
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


@views.route("/contact")
def contact():
    return render_template("contact.html", user=current_user)

@views.route("/resources",)
def resources():
    return render_template("resources.html")

@views.route('/Memorivise', methods=['POST', 'GET'])
def Memorivise():
    if Memorivise.method == 'POST':
        memorivise_document = request.form['document']
        new_revise = Revise( memorivise=memorivise_document)

        try:
            db.session.add(new_revise)
            db.session.commit()
            return redirect('/Memorivise')
        except:
            return "there was some problem adding the content."

    else:
        revisions = Revise.query.order_by(Memorivise.date).all()
        return render_template('memorivise.html', revisions=revisions)

@views.route('/Books')
def Books():
    return render_template('books.html')

@views.route('/transcribe')
def transcribe_speech():
    text = transcribe()
    return jsonify({'text': text})