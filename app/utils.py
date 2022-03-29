from flask import session

from app.models import Order

def get_orders():
    orders = Order.query.filter_by(client_id=session['_user_id'], closed=False).all()

    orders_j = [order.serialize() for order in orders]

    session['orders'] = orders_j