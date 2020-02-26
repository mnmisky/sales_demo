from main import db
import datetime

class Stock(db.Model):
    __tablename__='new_stock'
    id = db.Column(db.Integer, primary_key=True)
    inv_id = db.Column(db.Integer, db.ForeignKey('newinventories.id'))
    stock = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
