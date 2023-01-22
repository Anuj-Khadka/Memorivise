from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)
db.app = app


class revise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'{self.id} - {self.text}'




@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        revise_title = request.form['title']
        revise_description = request.form['description']
        new_revise = revise(title = revise_title, description=revise_description)

        try:
            db.session.add(new_revise)
            db.session.commit()
            return redirect('/')
        except:
            return "there was some problem adding the content."

    else:
        revisions = revise.query.order_by(revise.date).all()
        return render_template('index.html', revisions=revisions)



@app.route("/delete/<int:id>")
def delete(id):
    card_to_delete = revise.query.get(id)

    try:
        db.session.delete(card_to_delete)
        db.session.commit()
        return redirect("/")

    except:
        return "there was a problem deleting the card."
    



if __name__=="__main__":
    app.run(debug=True)

