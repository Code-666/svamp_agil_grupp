from flask import Flask
from flask import render_template, request, flash, redirect, url_for, session
from models import Mushroom, MushroomImage, MushroomInfo, db, app
from io import BytesIO
import base64
from flask_sqlalchemy import SQLAlchemy


# our main page
@app.route("/")
def mainpage():
    return render_template("mainpage.html")


# The filter search endpoint
@app.route("/min_svamp", methods=["GET", "POST"])
def min_svamp():
    # have to instantiate these variables else you get unrecognized variable error
    image_data_list = []
    name = None
    # session object lets you pass information between routes in flask
    # I use it to keep track has a form submitted or not
    form_submitted = session.get("form_submitted", False)

    if request.method == "POST":
        session["form_submitted"] = True
        # get the fields from the user form (radio buttons)
        form_submitted = session["form_submitted"]
        color = request.form.get("color")
        size = request.form.get("size")
        shape = request.form.get("shape")

        # This does a dynamic query based on what the user has selected
        query = Mushroom.query
        # Add filter conditions for the selected form fields that are not "Other"
        if color and color != "other":
            query = query.filter_by(color=color)
        if size and size != "other":
            query = query.filter_by(size=size)
        if shape and shape != "other":
            query = query.filter_by(shape=shape)

        mushrooms = query.all()
        for i in mushrooms:
            name = i.name
            break

        # i use the mushroomImage foreign key to get the correct images (this gets all images based on the mushroom name)
        images = MushroomImage.query.filter_by(mushroom_id=name).all()

        mushroom_images = MushroomImage.query.filter_by(mushroom_id=name).all()
        # This loop converts the image from the MushroomImage table from binary into utf-8
        # and al lthe images are added to the image_data_list which is sent to the template
        for img in mushroom_images:
            print(img.mushroom_id)
            image_data = img.image
            image_data_base64 = base64.b64encode(image_data).decode("utf-8")
            image_data_list.append(image_data_base64)

    # images are the MushroomImages instances
    # name is the name of the mushroom that the user has clicked on
    # form_submitted keeps track if there is a form post
    return render_template(
        "min_svamp.html",
        images=image_data_list,
        name=name,
        form_submitted=form_submitted,
    )


# the result page (when the user clicks on a mushroom to learn more about it)
# <mushroom_name> sends the Variable in the url (dont get how this works really)
@app.route("/result/<mushroom_name>")
def result(mushroom_name):
    session["form_submitted"] = False
    form_submitted = session["form_submitted"]

    # use the mushroom name to get the mushromInfo instance so that we can display >>>
    # more info on the result page if we like
    mushroom = Mushroom.query.filter_by(name=mushroom_name).first()

    # mushroom_name is the name of the mushroom that the user clicked on
    # mushroom_instance is the mushroomInfo instance for that mushroom name
    return render_template(
        "result.html", mushroom_name=mushroom_name, mushroom_instance=mushroom
    )


if __name__ == "__main__":
    app.run(debug=True)
