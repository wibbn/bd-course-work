from flask import session, render_template, request, redirect, jsonify
from app import app, db
from app.models import Item, Book, Order, Client
from app.utils import get_orders
		
@app.route('/order/add_item', methods=['POST'])
def add_item_to_order():
    try:
        book_id = request.form['book_id']
        lib_id = request.form['lib_id']
        next_path = request.form['next_path']

        if book_id and request.method == 'POST':
            item = Item.query.filter_by(book_id=book_id, library_id=lib_id, order_id=None).first().serialize()

            session.modified = True

            if 'cart' not in session or session['cart'] is None:
                session['cart'] = []

            if item['book_id'] not in [x['book_id'] for x in session['cart']]:
                session['cart'].append(item)

            return redirect(next_path)

        else:			
            raise RuntimeError()

    except Exception as e:
        print(e)

@app.route('/order/empty')
def empty_cart():
	try:
		session.clear()
		return redirect('/')
	except Exception as e:
		print(e)

@app.route('/order/submit')
def submit_order():
    if 'cart' not in session or len(session['cart']) == 0:
        return redirect('/')

    try:
        cart = session['cart']
        order = Order(
            message="",
            client=session['_user_id']
        )

        db.session.add(order)
        db.session.commit()

        Item.query.filter(Item.id.in_([x['id'] for x in cart])).update(
            {'order_id': order.id}
        )
        db.session.commit()

        session['cart'] = []

        return redirect('/order/current')
        
    except Exception as e:
        return(str(e))

@app.route('/order/get')
def get_session():
    return jsonify(session)

@app.route('/order')
def view_order():
    cart = session['cart']

    books = Book.query.filter(Book.id.in_([x['book_id'] for x in cart])).all()

    return render_template('order.html', books=books)

@app.route('/order/current')
def current_orders():
    get_orders()
    orders = []
    for order in session['orders']:
        items = Item.query.filter_by(order_id=order['id']).all()
        items_book_id = [item.serialize()['book_id'] for item in items]
        books = Book.query.filter(Book.id.in_(items_book_id)).all()
        # order['books'] = books

        order_out = {**order, 'books': books}

        orders.append(order_out)

    return render_template('current_orders.html', orders=orders)

@app.route('/admin/order/close', methods=['POST'])
def close_order():
    order_id = request.form['order_id']

    Item.query.filter_by(order_id=order_id).update({'order_id': None})
    Order.query.filter_by(id=order_id).update({'closed':True})
    
    db.session.commit()

    return redirect('/admin/orders')

@app.route('/admin/orders')
def all_orders():
    orders = Order.query.all()
    open_orders = []
    close_orders = []
    for order in orders:
        items = Item.query.filter_by(order_id=order.id).all()
        items_book_id = [item.serialize()['book_id'] for item in items]

        books = Book.query.filter(Book.id.in_(items_book_id)).all()
        client = Client.query.filter_by(id=order.client_id).first()

        if order.closed:
            close_orders.append({'order': order, 'client': client})
        else:
            open_orders.append({'order': order, 'books': books, 'client': client})

    return render_template('admin_orders.html', open_orders=open_orders, close_orders=close_orders)
    