class Mushroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    Traits = db.Column(db.Text)
    image = db.relationship("MushroomImage", backref="mushroom", lazy=True)


class MushroomImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary)
    mushroom_id = db.Column(db.Integer, db.ForeignKey("mushroom.name"))