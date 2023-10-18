from io import BytesIO
import base64
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db_name = "svampDB_222"
app.secret_key = "123abc"  # there are so many ways to store secret key. It is needed for session object to work.
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"sqlite:///{app.root_path}/instance/{db_name}.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# our model. i dont think these need to be explained in more detail (just ask)
class MushroomFilter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(100), unique=True)
    latin = db.Column(db.String(100), unique=True)
    giftig = db.Column(db.String(50))
    färg = db.Column(db.String(50))
    hatt = db.Column(db.String(50))
    skivor = db.Column(db.String(50))
    fot = db.Column(db.String(50))
    ring = db.Column(db.String(50))
    strumpa = db.Column(db.String(50))
    lukt = db.Column(db.String(50))
    bild = db.relationship("MushroomImage", backref="mushroom_filter", lazy=True)
    info = db.relationship("MushroomInfo", backref="mushroom_filter", lazy=True)


class MushroomImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bild = db.Column(db.LargeBinary)
    svamp_id = db.Column(db.Integer, db.ForeignKey("mushroom_filter.namn"))


class MushroomInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    beskrivning = db.Column(db.Text)
    svamp_id = db.Column(db.Integer, db.ForeignKey("mushroom_filter.namn"))


with app.app_context():
    db.create_all()
