from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
# from market import db, app




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name =  db.Column(db.String(length=30), nullable=False,unique=True)
    price = db.Column(db.Integer(),nullable=False)
    barcode =  db.Column(db.String(length=12), nullable=False,unique=True)
    description =  db.Column(db.String(length=1024), nullable=False,unique=True)

    # Optional function that will allow the information from 'dbTable.query.all()' to load in a particular format
    def __repr__(self):
        return f'Item{self.name}' 

""" Creating and Managing the database """
# $ python
# >>> from market import app, db
# >>> app.app_context().push()
# >>> db.create_all()
# >>> item1 = item1 = Item(name="Iphone 10",price= "800",barcode="1232456738495",description="decs")
# >>> item2 = item1 = Item(name="Laptop",price= "1200",barcode="7483938495734",description="laptop desc")
# >>> db.session.add(item1)
# >>> db.session.commit()
# >>> Item.query.all()  #This will show if the item was added.

"""=================================="""
    
with app.app_context():
    db.create_all()


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

    items = Item.query.all()

    return render_template('market.html', items = items)
if __name__ == '__main__':
    app.run(debug=True)
