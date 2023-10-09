# Johns branch
from flask import Flask
from flask import render_template, request, flash, redirect, url_for
import pandas as pd
import csv

app = Flask(__name__)

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

#Test av inlag av svampar
@app.route('/add-choice', methods=['POST'])
def add_choice():
    name = request.form['svamp']
    poison = request.form['giftig']
    img_name = request.form['img_nanm']
    traits = request.form['filter']
    new_row = {'Name': name, 'Poison': poison, 'Img_name': img_name, 'Traits': traits}
    data = pd.read_csv("Svampar.csv")
    data = data.append(new_row, ignore_index=True)
    data.to_csv('Svampar.csv', index=False)

    return render_template('mainpage.html', tables=[data.to_html()], titles=[''])





if __name__ == "__main__":
    app.run(debug=True)
