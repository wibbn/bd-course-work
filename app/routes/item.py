from flask import request, jsonify
from app import app, db, Item

@app.route("/item/create")
def add_item():
    book_id=request.args.get('book_id')
    library_id=request.args.get('library_id')
    try:
        item=Item(
            book= book_id,
            library=library_id
        )
        db.session.add(item)
        db.session.commit()
        return "Item added. Item id={}".format(item.id)
    except Exception as e:
	    return(str(e))

@app.route("/item/getall")
def get_all_items():
    try:
        items=Item.query.all()
        return jsonify([e.serialize() for e in items])
    except Exception as e:
	    return(str(e))

@app.route("/item/get/<id_>")
def get_item_by_id(id_):
    try:
        item=Item.query.filter_by(id=id_).first()
        return jsonify(item.serialize())
    except Exception as e:
	    return(str(e))