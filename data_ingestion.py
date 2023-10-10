from models import db, Mushroom, MushroomImage, MushroomInfo
from sqlalchemy.orm import query, join
from sqlalchemy import join
from sqlalchemy.orm import joinedload
import io
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
db_name = "svampDB_1"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"sqlite:///{app.root_path}/instance/{db_name}.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


def insert_data():
    svampar = [
        Mushroom(name="kantarell", color="green", size="small", shape="circle"),
        Mushroom(name="flugsvamp", color="red", size="big", shape="square"),
        Mushroom(name="champinjon ", color="red", size="small", shape="triangle"),
        Mushroom(name="Mushroom4", color="green", size="big", shape="triangle"),
        Mushroom(name="Mushroom5", color="green", size="medium", shape="square"),
        Mushroom(name="Svamp6", color="blue", size="small", shape="circle"),
        Mushroom(name="Svamp7", color="red", size="medium", shape="square"),
        Mushroom(name="Svamp8", color="red", size="big", shape="circle"),
    ]
    db.session.add_all(svampar)
    db.session.commit()

    def convertToBinaryData(filename):
        with open(filename, "rb") as file:
            blobData = file.read()
        return blobData

    img1 = r"C:\Users\Magnus\Desktop\images\m1.jpg"
    img2 = r"C:\Users\Magnus\Desktop\images\m2.jpg"
    img3 = r"C:\Users\Magnus\Desktop\images\m3.jpg"
    img4 = r"C:\Users\Magnus\Desktop\images\m4.jpg"

    image_data1 = convertToBinaryData(img1)
    image_data2 = convertToBinaryData(img2)
    image_data3 = convertToBinaryData(img3)
    image_data4 = convertToBinaryData(img4)

    images = [
        MushroomImage(image=image_data1, mushroom_id="kantarell"),
        MushroomImage(image=image_data2, mushroom_id="flugsvamp"),
        MushroomImage(image=image_data3, mushroom_id="champinjon"),
        MushroomImage(image=image_data4, mushroom_id="kantarell"),
    ]
    # # Add the Mushroom objects to the database
    db.session.add_all(images)
    db.session.commit()

    mushroomDesc = [
        MushroomInfo(
            similar="m1, m3, m8",
            description="The Kantarell mushroom, also known as the cantharellus cibarius, is a species of agaric fungus. It's known for its distinctive umbrella-shaped cap and white gills. The cap is smooth, convex, and cream-colored when young, becoming brownish and cracking into irregularly shaped, brownish-gray scales. The gills are free, broadly adnate to slightly decurved, and sometimes confluent. The mushroom has a mild, nutty flavor and is much prized for its excellent culinary qualities. It can be used in a variety of dishes, from soups to stews, as well as in pies and sauces.",
            mushroom_id="kantarell",
        ),
        MushroomInfo(
            similar="m4, m9, m9",
            description="The Fluegelsvamp mushroom, also known as the Pleurotus ostreatus, is a species of agaric fungus. It's known for its distinctive white cap and brown stem. The cap is convex and sometimes umbonate (with a slight depression in the center), and the gills are free, adnate to slightly decurved, and sometimes confluent. The mushroom has a mild, nutty flavor and is much prized for its excellent culinary qualities. It can be used in a variety of dishes, from soups to stews, as well as in pies and sauces.",
            mushroom_id="flugsvamp",
        ),
        MushroomInfo(
            similar="m4, m8, m1",
            description="The Champignon mushroom, also known as the Agaricus bisporus, is a species of agaric fungus. It's known for its distinctive umbrella-shaped cap and white gills. The cap is convex, often with a slight central depression, and the gills are free, broadly adnate to slightly decurved, and sometimes confluent. The mushroom has a mild, nutty flavor and is much prized for its excellent culinary qualities. It can be used in a variety of dishes, from soups to stews, as well as in pies and sauces.",
            mushroom_id="champinjon",
        ),
        MushroomInfo(
            similar="m7",
            description="The Mushroom4 mushroom, also known as the Agaricus bisporus, is a species of agaric fungus. It's known for its distinctive umbrella-shaped cap and white gills. The cap is convex, often with a slight central depression, and the gills are free, broadly adnate to slightly decurved, and sometimes confluent. The mushroom has a mild, nutty flavor and is much prized for its excellent culinary qualities. It can be used in a variety of dishes, from soups to stews, as well as in pies and sauces.",
            mushroom_id="Mushroom4",
        ),
        MushroomInfo(
            similar="m11, m12",
            description="The Mushroom5 mushroom, also known as the Agaricus bisporus, is a species of agaric fungus. It's known for its distinctive umbrella-shaped cap and white gills. The cap is convex, often with a slight central depression, and the gills are free, broadly adnate to slightly decurved, and sometimes confluent. The mushroom has a mild, nutty flavor and is much prized for its excellent culinary qualities. It can be used in a variety of dishes, from soups to stews, as well as in pies and sauces.",
            mushroom_id="Mushroom5",
        ),
        MushroomInfo(
            similar="m1, m2",
            description="The Svamp6 mushroom, also known as the Agaricus bisporus, is a species of agaric fungus. It's known for its distinctive umbrella-shaped cap and white gills. The cap is convex, often with a slight central depression, and the gills are free, broadly adnate to slightly decurved, and sometimes confluent. The mushroom has a mild, nutty flavor and is much prized for its excellent culinary qualities. It can be used in a variety of dishes, from soups to stews, as well as in pies and sauces.",
            mushroom_id="Svamp6",
        ),
        MushroomInfo(
            similar="m6, m7",
            description="The Svamp7 mushroom, also known as the Agaricus bisporus, is a species of agaric fungus. It's known for its distinctive umbrella-shaped cap and white gills. The cap is convex, often with a slight central depression, and the gills are free, broadly adnate to slightly decurved, and sometimes confluent. The mushroom has a mild, nutty flavor and is much prized for its excellent culinary qualities. It can be used in a variety of dishes, from soups to stews, as well as in pies and sauces.",
            mushroom_id="Svamp7",
        ),
        MushroomInfo(
            similar="m1, m8",
            description="The Svamp8 mushroom, also known as the Agaricus bisporus, is a species of agaric fungus. It's known for its distinctive umbrella-shaped cap and white gills. The cap is convex, often with a slight central depression, and the gills are free, broadly adnate to slightly decurved, and sometimes confluent. The mushroom has a mild, nutty flavor and is much prized for its excellent culinary qualities. It can be used in a variety of dishes, from soups to stews, as well as in pies and sauces.",
            mushroom_id="Svamp8",
        ),
    ]
    db.session.add_all(mushroomDesc)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        insert_data()
