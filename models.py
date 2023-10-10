from io import BytesIO
import base64
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
db_name = "svampDB_1"
app.secret_key = "123abc"  # there are so many ways to store secret key. It is needed for session object to work.
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"sqlite:///{app.root_path}/instance/{db_name}.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# our model. i dont think these need to be explained in more detail (just ask)
class Mushroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    color = db.Column(db.String(50))
    size = db.Column(db.String(50))
    shape = db.Column(db.String(50))
    image = db.relationship("MushroomImage", backref="mushroom", lazy=True)
    info = db.relationship("MushroomInfo", backref="mushroom", lazy=True)


class MushroomImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary)
    mushroom_id = db.Column(db.Integer, db.ForeignKey("mushroom.name"))


class MushroomInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    similar = db.Column(db.String(50))
    description = db.Column(db.Text)
    mushroom_id = db.Column(db.Integer, db.ForeignKey("mushroom.name"))


with app.app_context():
    db.create_all()
