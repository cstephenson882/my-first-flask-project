from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from market.models import Item
from market import app


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/market')
def market_page():
    # items = [
    #     {'id': 1, 'name': 'Product A', 'barcode': '123456789012', 'price': 10},
    #     {'id': 2, 'name': 'Product B', 'barcode': '234567890123', 'price': 20},
    #     {'id': 3, 'name': 'Product C', 'barcode': '345678901234', 'price': 30}
    # ]
    """This line below will get the info from the database"""
    items = Item.query.all()

    return render_template('market.html', items = items)