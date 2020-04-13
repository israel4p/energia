from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Valor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kwAtual = db.Column(db.Integer)
    data = db.Column(db.String(10))
    kwValor = db.Column(db.String(10))
    kwTotal = db.Column(db.String(10))
    totalPagar = db.Column(db.String(10))


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10))
    password = db.Column(db.String(128))

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
