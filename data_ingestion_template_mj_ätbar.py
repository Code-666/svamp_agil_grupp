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
            namn="svart trumpetsvamp",
            latin="craterellus cornucopioides",
            giftig="nej",
            färg="svart",
            hatt="trattformad",
            skivor="rynkig",
            fot="sammanfogad",
            ring="NA",
            strumpa="NA",
            lukt="NA",
        ),
        MushroomFilter(
            namn="blek taggsvamp",
            latin="hydnum repandum",
            giftig="nej",
            färg="vit",
            hatt="konvex",
            skivor="taggig",
            fot="sidoställd",
            ring="NA",
            strumpa="NA",
            lukt="NA",
        ),
        MushroomFilter(
            namn="blodchampinjon",
            latin="agaricus langei",
            giftig="nej",
            färg="ljusbrun",
            hatt="konkav",
            skivor="NA",
            fot="tjock",
            ring="tunn",
            strumpa="NA",
            lukt="NA",
        ),
        MushroomFilter(
            namn="blomkålssvamp",
            latin="sparassis crispa",
            giftig="nej",
            färg="gräddfärgad",
            hatt="blomkål",
            skivor="NA",
            fot="rotlik",
            ring="NA",
            strumpa="NA",
            lukt="frisk",
        ),
        MushroomFilter(
            namn="mandelriska",
            latin="lactarius volemus",
            giftig="nej",
            färg="orange",
            hatt="konkav",
            skivor="täta",
            fot="NA",
            ring="NA",
            strumpa="NA",
            lukt="skaldjur",
        ),
    ]

    db.session.add_all(svampar)
    db.session.commit()

    def convertToBinaryData(filename):
        with open(filename, "rb") as file:
            blobData = file.read()
        return blobData

    # change to where the pictures are on your pc (or webb)
    img1 = r"C:\Users\Magnus\Desktop\mj-branch-333\svamp_agil_grupp\svampbilder\ä1.jpg"
    img2 = r"C:\Users\Magnus\Desktop\mj-branch-333\svamp_agil_grupp\svampbilder\ä2.jpg"
    img3 = r"C:\Users\Magnus\Desktop\mj-branch-333\svamp_agil_grupp\svampbilder\ä3.jpg"
    img4 = r"C:\Users\Magnus\Desktop\mj-branch-333\svamp_agil_grupp\svampbilder\ä4.jpg"
    img5 = r"C:\Users\Magnus\Desktop\mj-branch-333\svamp_agil_grupp\svampbilder\ä5.jpg"

    image_data1 = convertToBinaryData(img1)
    image_data2 = convertToBinaryData(img2)
    image_data3 = convertToBinaryData(img3)
    image_data4 = convertToBinaryData(img4)
    image_data5 = convertToBinaryData(img5)

    images = [
        MushroomImage(bild=image_data1, svamp_id="svart trumpetsvamp"),
        MushroomImage(bild=image_data2, svamp_id="blek taggsvamp"),
        MushroomImage(bild=image_data3, svamp_id="blodchampinjon"),
        MushroomImage(bild=image_data4, svamp_id="blomkålssvamp"),
        MushroomImage(bild=image_data5, svamp_id="mandelriska"),
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
    # db.session.add_all(mushroomInfo)
    # db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        insert_data()
        print("data_ingestion script has run")
