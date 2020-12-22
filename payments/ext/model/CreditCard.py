from payments.ext.model import db

class CreditCard(db.Model):
    __tablename__ = "creditcard"
    id = db.Column("id", db.Integer, primary_key=True)
    exp_date = db.Column("exp_date",db.DateTime)
    holder = db.Column("holder",db.String(100))
    cc_number = db.Column("cc_number",db.LargeBinary)
    cvv = db.Column("cvv", db.Integer)