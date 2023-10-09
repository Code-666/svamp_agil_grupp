# Johns branch
from flask import Flask
from flask import render_template, request, flash, redirect, url_for
import pandas as pd
import csv

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class Mushroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    traits = db.Column(db.Text)
    image = db.relationship("MushroomImage", backref="mushroom", lazy=True)


class MushroomImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary)
    mushroom_id = db.Column(db.Integer, db.ForeignKey("mushroom.name"))

#Sebbe Är bra
@app.route("/")
def hello_world():
    return "<p>Hello, world and Svampar</p>"


@app.route("/test")
def test():
    return "<p>Hello, Svamp. new endpoint.</p>"


@app.route("/svamp")
def svamp():
    return "<p> Hello, Svampälskare. </p>"


@app.route("/mj_test")
def mj_test():
    """
    ...
    """
    return render_template("mj_test.html")


@app.route("/mainpage")
def mainpage():
    """
    ...
    """
    return render_template("mainpage.html")

@app.route("/admin")
def admin():



    return render_template("admin.html")


@app.route('/add-choice', methods=['POST'])
def add_choice():
    name = request.form['svamp']
    poison = request.form['giftig']
    img_name = request.form['img_nanm']
    traits = request.form['filter']
    #imgage_file = request.form["myfile"]
    #new_row = {'Name': name, 'Poison': poison, 'Img_name': img_name, 'Traits': traits}
    #data = pd.read_csv("Svampar.csv")

    # Add the new row to the DataFrame
    #data = data.append(new_row, ignore_index=True)

    # Save the updated DataFrame to the CSV file
    #data.to_csv('Svampar.csv', index=False)

    # spara imgagen till pathen static/pics

    svamp = Mushroom(name=name, traits=traits)
    db.session.add(svamp)
    db.session.commit()

    return render_template('mainpage.html')





if __name__ == "__main__":
    app.run(debug=True)
