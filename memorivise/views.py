from flask import Flask, Blueprint, render_template, request, redirect, flash, jsonify
from sqlalchemy import engine
from .models import Revise, Contact, MemoriviseDB
from .speech import transcribe
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


@views.route("/revise/revise_test", methods=["POST", "GET"])
def revise_test():
    if request.method == 'POST':
        user_data = request.form['revise_test'].lower()
        # this will check case sensetive
        # result = db.session.query(Revise).filter(
        #     Revise.description == user_data).all()

        # this is case insensetive check
        result = db.session.query(Revise).filter(
            Revise.description.ilike(user_data)).all()
        if result:
            flash("yes it is correct", category="success")
            return redirect("/revise")
        else:
            flash("no try again", category="error")
            return redirect("/revise")
    return render_template('revise.html', user=current_user)


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


@views.route("/resources",)
def resources():
    return render_template("resources.html")


@views.route('/memorivise', methods=['POST', 'GET'])
def Memorivise():
    if request.method == 'POST':
        memorivise_title = request.form['title']
        memorivise_document = request.form['document']
        new_memorevise = MemoriviseDB(
            title=memorivise_title, document=memorivise_document)

        try:
            db.session.add(new_memorevise)
            db.session.commit()
            return redirect('/memorivise')
        except:
            return "there was some problem adding the content."

    else:
        revisions = MemoriviseDB.query.order_by(MemoriviseDB.date).all()
        return render_template('memorivise.html', revisions=revisions, user=current_user)


@views.route("/memorivise/memorivise_test", methods=["POST", "GET"])
def memorivise_test():
    if request.method == 'POST':
        user_data = request.form['memorivise_test'].lower()

        # this is case insensetive check
        result = db.session.query(MemoriviseDB).filter(
            MemoriviseDB.document.ilike(user_data))
        if result:
            flash("yes it is correct", category="success")
            return redirect("/memorivise")
        else:
            flash("no try again", category="error")
            return redirect("/memorivise")
    return render_template('memorivise.html', user=current_user)


@views.route("/memorivise/delete/<int:id>")
def memorivise_delete(id):
    card_to_delete = MemoriviseDB.query.get(id)

    try:
        db.session.delete(card_to_delete)
        db.session.commit()
        flash("Test card deleted successfully!", category="success")
        return redirect("/memorivise")

    except:
        return "there was a problem deleting the card."


@views.route("/memorivise/update/<int:id>", methods=['POST', 'GET'])
def memorivise_update(id):
    update = MemoriviseDB.query.get_or_404(id)

    if request.method == 'POST':
        update.title = request.form['title']
        update.document = request.form['document']

        try:
            db.session.commit()
            flash("Test card updated successfully!", category="success")
            return redirect('/memorivise')

        except:
            return "Sorry! there was a problem updating the card"

    else:
        return render_template("update_memorivise.html", update=update, user=current_user)


@views.route('/books')
def Books():
    return render_template('books.html', user=current_user)


@views.route('/science')
def Science():
    return render_template('science.html', user=current_user)


@views.route('/physics')
def Physics():
    return render_template('physics.html', user=current_user)


@views.route('/biology')
def Biology():
    return render_template('biology.html', user=current_user)


@views.route('/chemistry')
def Chemistry():
    return render_template('chemistry.html', user=current_user)


@views.route('/studygames')
def studygames():
    return render_template('studygames.html', user=current_user)


@views.route('/personalbook')
def personalbook():
    return render_template('personalbook.html', user=current_user)


@views.route('/learning')
def learning():
    return render_template('learning.html', user=current_user)


@views.route('/quiz')
def quiz():
    return render_template('quiz.html', user=current_user)

@views.route('/class8')
def class8():
    return render_template('class8.html', user=current_user)

@views.route('/class9')
def class9():
    return render_template('class9.html', user=current_user)

@views.route('/class10')
def class10():
    return render_template('class10.html', user=current_user)

@views.route('/class11science')
def class11science():
    return render_template('class11science.html', user=current_user)

@views.route('/simulations')
def simulations():
    return render_template('simulations.html', user=current_user)

@views.route('/sat')
def sat():
    return render_template('sat.html', user=current_user)

@views.route('/solar')
def solar():
    return render_template('solar.html', user=current_user)



@views.route('/transcribe')
def transcribe_speech():
    text = transcribe()
    return jsonify({'text': text})
