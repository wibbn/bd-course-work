from app import db

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    library_id = db.Column(db.Integer, db.ForeignKey('library.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

    def __init__(self, book, library):
        self.book_id = book
        self.library_id = library

    def __repr__(self):
        return '<Item {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'book_id': self.book_id,
            'library_id': self.library_id,
            'order_id': self.order_id
        }