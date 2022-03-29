from flask import request
from app import *

@app.route("/user/create")
def add_client():
    first_name=request.args.get('first_name')
    last_name=request.args.get('last_name')
    phone_number=request.args.get('phone_number')
    email=request.args.get('email')
    try:
        client=Client(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email
        )
        db.session.add(client)
        db.session.commit()
        return "User added. User id={}".format(client.id)
    except Exception as e:
	    return(str(e))

@app.route("/user/getall")
def get_all_clients():
    try:
        clients=Client.query.all()
        return jsonify([e.serialize() for e in clients])
    except Exception as e:
	    return(str(e))

@app.route("/user/get/<id_>")
def get_client_by_id(id_):
    try:
        client=Client.query.filter_by(id=id_).first()
        return jsonify(client.serialize())
    except Exception as e:
	    return(str(e))