# Johns branch
from flask import Flask
from flask import render_template, request, flash, redirect, url_for
import os
import pandas as pd
import csv
import base64

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'mydatabase.db')
db = SQLAlchemy(app)

# Define a function to encode binary data in base64
def base64_encode(data):
    return base64.b64encode(data).decode('utf-8')

# Register a custom Jinja2 filter for base64 encoding
app.jinja_env.filters['base64_encode'] = base64_encode

class Mushroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    traits = db.Column(db.Text)
    image_data = db.Column(db.LargeBinary)
    poison = db.Column(db.Boolean, default=False)  # New boolean column for poison

    def __init__(self, name, traits, image_data=None, poison=False):
        self.name = name
        self.traits = traits
        self.image_data = image_data
        self.poison = poison

    def get_image_data(self):
        return self.image_data


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
    mushrooms = Mushroom.query.all()
    return render_template("admin.html", mushrooms=mushrooms)


@app.route('/add-choice', methods=['POST'])
def add_choice():
    file = request.files['image']
    name = request.form['svamp']
    traits = request.form['filter']
    poison = True
    if request.form['poison'] == 'True':
        poison = True
    elif request.form['poison'] == 'False':
        poison = False

    #imgage_file = request.form["myfile"]
    #new_row = {'Name': name, 'Poison': poison, 'Img_name': img_name, 'Traits': traits}
    #data = pd.read_csv("Svampar.csv")

    # Add the new row to the DataFrame
    #data = data.append(new_row, ignore_index=True)

    # Save the updated DataFrame to the CSV file
    #data.to_csv('Svampar.csv', index=False)

    # spara imgagen till pathen static/pics

    image_data = file.read()
    mushroom = Mushroom(name=name, traits=traits, image_data=image_data, poison=poison)
    db.session.add(mushroom)
    db.session.commit()
    return redirect(url_for('admin'))





if __name__ == '__main__':
    app.secret_key = 'your_secret_key'  # Replace with your secret key
    app.run(debug=True)
