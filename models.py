from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.String(80), nullable=False)
    terms = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'User({self.username},{self.email})'
