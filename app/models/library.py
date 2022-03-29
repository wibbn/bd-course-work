from app import db

class Library(db.Model):
    __tablename__ = 'library'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    state = db.Column(db.String())
    city = db.Column(db.String())
    street = db.Column(db.String())
    building = db.Column(db.String())
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    items = db.relationship('Item', backref='library', lazy=True)

    def __init__(self, name, state, city, street, building, latitude, longitude):
        self.name = name
        self.state = state
        self.city = city
        self.street = street
        self.building = building
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f'<Library {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'state': self.state,
            'city': self.city,
            'street': self.street,
            'building': self.building,
            'message': self.message,
            'items': self.items
        }

    def toJSON(self):
        return self.serialize()