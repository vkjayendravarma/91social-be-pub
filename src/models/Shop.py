from src import db

class Shop(db.Document):
    name = db.StringField()
    coordinates = db.PointField()