from flask import request, jsonify, render_template
from app import app, db, Library

@app.route("/library/create")
def add_library():
    name=request.args.get('name')
    state=request.args.get('state')
    city=request.args.get('city')
    street=request.args.get('street')
    building=request.args.get('building')
    latitude=request.args.get('latitude')
    longitude=request.args.get('longitude')
    try:
        library=Library(
            name= name,
            state= state,
            city= city,
            street= street,
            building= building,
            latitude= latitude,
            longitude= longitude
        )
        db.session.add(library)
        db.session.commit()
        return "Library added. Library id={}".format(library.id)
    except Exception as e:
	    return(str(e))

@app.route("/libs")
def get_library_list():
    try:
        libraries=Library.query.all()
        return render_template('libraries.html', data=libraries)
    except Exception as e:
	    return(str(e))

@app.route("/library/getall")
def get_all_libraries():
    try:
        libraries=Library.query.all()
        return jsonify([e.serialize() for e in libraries])
    except Exception as e:
	    return(str(e))

@app.route("/library/get/<id_>")
def get_library_by_id(id_):
    try:
        library=Library.query.filter_by(id=id_).first()
        return jsonify(library.serialize())
    except Exception as e:
	    return(str(e))