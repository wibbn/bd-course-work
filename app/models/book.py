from app import db

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())
    category = db.Column(db.String())
    items = db.relationship('Item', backref='book', lazy=True)

    def __init__(self, name, author, published='', category=''):
        self.name = name
        self.author = author
        self.published = published
        self.category = category

    def __repr__(self):
        return f'<Book {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'author': self.author,
            'published': self.published,
            'category': self.category
        }

    def toJSON(self):
        return self.serialize()