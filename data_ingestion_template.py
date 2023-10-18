from models import db, MushroomFilter, MushroomImage, MushroomInfo
from sqlalchemy.orm import query, join
from sqlalchemy import join
from sqlalchemy.orm import joinedload
import io
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
db_name = "svampDB_222"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"sqlite:///{app.root_path}/instance/{db_name}.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# This is for populating the database for testing
def insert_data():
    svampar = [
        MushroomFilter(
            namn="",
            latin="",
            giftig="",
            färg="",
            hatt="",
            skivor="",
            fot="",
            ring="",
            strumpa="",
            lukt="",
        ),
        MushroomFilter(
            namn="",
            latin="",
            giftig="",
            färg="",
            hatt="",
            skivor="",
            fot="",
            ring="",
            strumpa="",
            lukt="",
        ),
    ]

    db.session.add_all(svampar)
    db.session.commit()

    def convertToBinaryData(filename):
        with open(filename, "rb") as file:
            blobData = file.read()
        return blobData

    # change to where the pictures are on your pc (or webb)
    img1 = r"path to your image"
    img2 = r"path to your image"

    image_data1 = convertToBinaryData(img1)
    image_data2 = convertToBinaryData(img2)

    images = [
        MushroomImage(bild=image_data1, svamp_id="same as MushroomFilter.name"),
        MushroomImage(bild=image_data2, svamp_id="same as MushroomFilter.name"),
    ]
    # # Add the Mushroom objects to the database
    db.session.add_all(images)
    db.session.commit()

    mushroomInfo = [
        MushroomInfo(
            beskrivning="""
            
            """,
            svamp_id="same as MushroomFilter.name",
        ),
        MushroomInfo(
            beskrivning=""""
            
            """,
            svamp_id="same as MushroomFilter.name",
        ),
    ]
    db.session.add_all(mushroomInfo)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        insert_data()
        print("data_ingestion script has run")
