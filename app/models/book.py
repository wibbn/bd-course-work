from app import db

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())
    category = db.Column(db.String())
    description = db.Column(db.String())
    items = db.relationship('Item', backref='book', lazy=True)

    def __init__(self, name, author, published='', category='', description=''):
        self.name = name
        self.author = author
        self.published = published
        self.category = category
        self.description = description

    def __repr__(self):
        return f'<Book {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'author': self.author,
            'published': self.published,
            'category': self.category,
            'description': self.description,
        }

    def toJSON(self):
        return self.serialize()