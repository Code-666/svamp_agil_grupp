from flask import Flask
from flask import render_template, request, flash, redirect, url_for, session
from models import MushroomFilter, MushroomImage, MushroomInfo, db, app
from io import BytesIO
import base64
from flask_sqlalchemy import SQLAlchemy


# our main page
@app.route("/")
@app.route("/mainpage")
def mainpage():
    return render_template("index.html")


@app.route("/galleri")
def galleri():
    mushrooms = MushroomFilter.query.all()
    return render_template("galleri.html", mushrooms=mushrooms)


@app.route("/dagens_svamp")
def dagens_svamp():
    return render_template("dagens_svamp.html")


# creates a function that converts the binary images on the frontend (in the jinja2)
def b64encode(s):
    return base64.b64encode(s).decode("utf-8")


# to use the function in jinja2 you have to add it to the jinja env like this:
app.jinja_env.filters["b64encode"] = b64encode


# The filter search endpoint
@app.route("/min_svamp", methods=["GET", "POST"])
def min_svamp():
    # have to instantiate these variables else you get unrecognized variable error
    image_data_list = []
    # if the query gets more than one result
    mushroom_names = []
    name = None
    svamp = None
    mushrooms = None
    # session object lets you pass information between routes in flask
    # I use it to keep track has a form submitted or not
    form_submitted = session.get("form_submitted", False)

    if request.method == "POST":
        session["form_submitted"] = True
        # get the fields from the user form (radio buttons)
        form_submitted = session["form_submitted"]
        färg = request.form.get("färg")
        hatt = request.form.get("hatt")
        skivor = request.form.get("skivor")
        fot = request.form.get("fot")
        # strumpa = request.form.get("strumpa")
        lukt = request.form.get("lukt")

        # This does a dynamic query based on what the user has selected in the form
        query = MushroomFilter.query
        # Add filter conditions for the selected form fields that are not "inget/annat"
        if färg and färg != "inget/annat":
            query = query.filter_by(färg=färg)
        if hatt and hatt != "inget/annat":
            query = query.filter_by(hatt=hatt)
        if skivor and skivor != "inget/annat":
            query = query.filter_by(skivor=skivor)
        if fot and fot != "inget/annat":
            query = query.filter_by(fot=fot)
        # if strumpa and strumpa != "inget/annat":
        #     query = query.filter_by(strumpa=strumpa)
        if lukt and lukt != "inget/annat":
            query = query.filter_by(lukt=lukt)

        mushrooms = query.all()

    # form_submitted keeps track if there is a form post
    # mushrooms is a list of all the mushroom instances that met the form search criteria
    return render_template(
        "min_svamp.html",
        form_submitted=form_submitted,
        mushrooms=mushrooms,
    )


# the result page (when the user clicks on a mushroom to learn more about it)
# <mushroom_name> sends the Variable in the url (dont get how this works really)
@app.route("/result/<mushroom_name>")
def result(mushroom_name):
    session["form_submitted"] = False
    form_submitted = session["form_submitted"]

    # use the mushroom name to get the mushromInfo instance so that we can display >>>
    # more info on the result page if we like
    mushroom = MushroomFilter.query.filter_by(namn=mushroom_name).first()

    # mushroom_name is the name of the mushroom that the user clicked on
    # mushroom_instance is the mushroomInfo instance for that mushroom name
    return render_template(
        "result.html", mushroom_name=mushroom_name, mushroom_instance=mushroom
    )


if __name__ == "__main__":
    app.run(debug=True)
