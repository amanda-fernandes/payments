from payments.ext.model import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    passwrd = db.Column(db.String(80))