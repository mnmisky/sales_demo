from main import db


class Inventories(db.Model):
    __tablename__='newinventories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(120),  nullable=False)
    bp = db.Column(db.Numeric(13,2))
    sp= db.Column(db.Numeric(13,2), nullable=False)
    stock = db.relationship('Stock', backref='inventories', lazy=True)
    sales = db.relationship('Sales', backref='inventories', lazy=True)
