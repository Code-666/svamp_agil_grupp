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
            namn="vårrödhätting",
            latin="entoloma vernum",
            giftig="ja",
            färg="mörkbrun",
            hatt="NA",
            skivor="glesa",
            fot="NA",
            ring="NA",
            strumpa="NA",
            lukt="luktlös",
        ),
        MushroomFilter(
            namn="svartriska",
            latin="lactarius necator",
            giftig="ja",
            färg="mörbrun",
            hatt="konkav",
            skivor="täta",
            fot="tjock",
            ring="NA",
            strumpa="NA",
            lukt="NA",
        ),
        MushroomFilter(
            namn="lokspindling",
            latin="cortinarius callisteus",
            giftig="ja",
            färg="blekgul",
            hatt="NA",
            skivor="täta",
            fot="Sidoställd",
            ring="NA",
            strumpa="NA",
            lukt="stenkol",
        ),
        MushroomFilter(
            namn="giftkremla",
            latin="russula emetica",
            giftig="ja",
            färg="röd",
            hatt="konvex",
            skivor="täta",
            fot="NA",
            ring="NA",
            strumpa="NA",
            lukt="fruktig",
        ),
        MushroomFilter(
            namn="klubbtrattskivling",
            latin="ampulloclitocybe clavipes",
            giftig="ja",
            färg="ljusbrun",
            hatt="konkav",
            skivor="nedlöpande",
            fot="NA",
            ring="NA",
            strumpa="NA",
            lukt="söt",
        ),
    ]

    db.session.add_all(svampar)
    db.session.commit()

    def convertToBinaryData(filename):
        with open(filename, "rb") as file:
            blobData = file.read()
        return blobData

    # change to where the pictures are on your pc (or webb)
    img1 = r"C:\Users\Magnus\Desktop\mj-branch-333\svamp_agil_grupp\svampbilder\g1.jpg"
    img2 = r"C:\Users\Magnus\Desktop\mj-branch-333\svamp_agil_grupp\svampbilder\g2.jpg"
    img3 = r"C:\Users\Magnus\Desktop\mj-branch-333\svamp_agil_grupp\svampbilder\g3.jpg"
    img4 = r"C:\Users\Magnus\Desktop\mj-branch-333\svamp_agil_grupp\svampbilder\g4.jpg"
    img5 = r"C:\Users\Magnus\Desktop\mj-branch-333\svamp_agil_grupp\svampbilder\g5.jpg"

    image_data1 = convertToBinaryData(img1)
    image_data2 = convertToBinaryData(img2)
    image_data3 = convertToBinaryData(img3)
    image_data4 = convertToBinaryData(img4)
    image_data5 = convertToBinaryData(img5)

    images = [
        MushroomImage(bild=image_data1, svamp_id="vårrödhätting"),
        MushroomImage(bild=image_data2, svamp_id="svartriska"),
        MushroomImage(bild=image_data3, svamp_id="lokspindling"),
        MushroomImage(bild=image_data4, svamp_id="giftkremla"),
        MushroomImage(bild=image_data5, svamp_id="klubbtrattskivling"),
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
