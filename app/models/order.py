from datetime import datetime
import json

from app import db
from app.models import Item

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String())
    open_time = db.Column(db.DateTime, default=datetime.now)
    number = db.Column(db.Integer, default=datetime.now().strftime('%f'))
    items = db.relationship('Item', backref='order', lazy=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    closed = db.Column(db.Boolean, default=False)

    def __init__(self, message, client):
        self.message = message
        self.client_id = client

    def __repr__(self):
        return '<Order {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id,
            'message': self.message,
            'open_time': self.open_time,
            'number': self.number,
            'client_id': self.client_id,
            'closed': self.closed
        }

    # def get(self):
    #     return self.serialize()

    # def __iter__(self):
    #     return self.serialize().iteritems()

    # def toJSON(self):
    #     return json.dumps(self.serialize(), default=lambda o: o.__dict__, 
    #         sort_keys=True, indent=4)