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
            namn="giftspindling",
            latin="galerina marginata",
            giftig="ja",
            färg="ljusbrun",
            hatt="konvex",
            skivor="nedlöpande",
            fot="luddig",
            ring="pruinös",
            strumpa="NA",
            lukt="NA",
        ),
        MushroomFilter(
            namn="aspsopp",
            latin="leccinum aurantiacum s.lat.",
            giftig="nej",
            färg="röd",
            hatt="konvex",
            skivor="rör",
            fot="tofsig",
            ring="NA",
            strumpa="NA",
            lukt="NA",
        ),
    ]

    db.session.add_all(svampar)
    db.session.commit()

    def convertToBinaryData(filename):
        with open(filename, "rb") as file:
            blobData = file.read()
        return blobData

    # change to where the pictures are on your pc (or webb)
    img1 = r"C:\Users\Magnus\Desktop\svampMapp\svamp_agil_grupp\svampbilder\m1.jpg"
    img2 = r"C:\Users\Magnus\Desktop\svampMapp\svamp_agil_grupp\svampbilder\m2.jpg"

    image_data1 = convertToBinaryData(img1)
    image_data2 = convertToBinaryData(img2)

    images = [
        MushroomImage(bild=image_data1, svamp_id="giftspindling"),
        MushroomImage(bild=image_data2, svamp_id="aspsopp"),
    ]
    # # Add the Mushroom objects to the database
    db.session.add_all(images)
    db.session.commit()

    mushroomInfo = [
        MushroomInfo(
            beskrivning="""    • Hatt som ung klockformig till välvd, senare mer plan, ofta med svag puckel, hygrofan, brun till gulbrun, i torka ljusare brungul.
    • Skivor vidväxta till nedlöpande, beige till ljusbruna.
    • Fot ljusbrun, mörkare mot fotbasen, med en tunn ring, ovanför ringen pruinös.
    • Hela foten är täckt med tunna lodräta vita fibrer som lätt försvinner vid tummning.
    • Doftar och smakar svagt mjölaktigt.

    En liten oansenlig skivling med en hattbredd som sällan överstiger 5 cm.  Förekommer över hela Norden och växer på barrved, ibland lövved, i skog, på barkningsplatser och på träflis längs motionsslingor.

Svampgift & giftverkan

    Innehåller Amatoxin, samma gift som förekommer i vit och lömsk flugsvamp.

Förväxlingssvampar

    Föränderlig tofsskivling - vanligtvis större, har utstående fjäll på foten, växer i klungor på stubbar av olika lövträd, matsvamp.
    Det finns flera snarlika brunsporiga och oätliga skivlingar.""",
            svamp_id="gifthätting",
        ),
        MushroomInfo(
            beskrivning=""""    • Hatt välvd, orange till rödbrun.
    • Hatthud överhängande (hänger någon mm utanför hattkanten).
    • Rör smutsvita.
    • Fot vit, med vita tofsar som med åldern mörknar till rödbrunt.
    • Kött i snitt rodnande, övergår sedan till svart.

    Växer med asp och förekommer över hela Norden.

Förväxlingssvampar

    Strävsoppar är ett komplex med flera närstående arter som kan likna varandra mycket. Som matsvampplockare behöver du inte kunna skilja dem alla åt eftersom alla är ätliga.

    Tegelsopp - Tegelröd hattfärg, har svarta tofsar på foten.""",
            svamp_id="aspsopp",
        ),
    ]
    db.session.add_all(mushroomInfo)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        insert_data()
        print("data_ingestion script has run")
