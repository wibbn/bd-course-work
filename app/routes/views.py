from flask import redirect, url_for, render_template
from jinja2 import TemplateNotFound

from flask_login import current_user

from app import app
from app.utils import get_orders


@app.route('/', defaults={'path': 'libs'})
@app.route('/<path>')
def index(path):

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    get_orders()

    try:    
        return redirect(path)
    except Exception as e:
        print(e)