from app import db
from flask_login import UserMixin

class Client(UserMixin, db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    phone_number = db.Column(db.String())
    email = db.Column(db.String())
    orders = db.relationship('Order', backref='client', lazy=True)

    def __init__(self, first_name, last_name, email, phone_number=''):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return '<Client {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'email': self.email,
            'orders': self.orders
        }

    def toJSON(self):
        return self.serialize()