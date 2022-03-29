from flask import request, jsonify, render_template
from app import app, db, Book, Item, Library

@app.route("/book/create")
def add_book():
    name=request.args.get('name')
    author=request.args.get('author')
    published=request.args.get('published')
    category=request.args.get('category')
    try:
        book=Book(
            name=name,
            author=author,
            published=published,
            category=category
        )
        db.session.add(book)
        db.session.commit()
        return "Book added. Book id={}".format(book.id)
    except Exception as e:
	    return(str(e))

@app.route("/book/getall")
def get_all_books():
    try:
        books=Book.query.all()
        return jsonify([e.serialize() for e in books])
    except Exception as e:
	    return(str(e))

@app.route("/books/atlib/<id_>")
def get_book_by_library_id(id_):
    try:
        books=db.session.query(Book).join(Item, Book.items).filter(Item.library_id == id_).filter(Item.order==None)
        lib = Library.query.filter_by(id=id_).first()
        return render_template('books.html', data=books, lib=lib)
    except Exception as e:
	    return(str(e))
