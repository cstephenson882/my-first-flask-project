
from market import db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name =  db.Column(db.String(length=30), nullable=False,unique=True)
    price = db.Column(db.Integer(),nullable=False)
    barcode =  db.Column(db.String(length=12), nullable=False,unique=True)
    description =  db.Column(db.String(length=1024), nullable=False,unique=True)

    # Optional function that will allow the information from 'dbTable.query.all()' to load in a particular format
    def __repr__(self):
        return f'Item{self.name}' 

