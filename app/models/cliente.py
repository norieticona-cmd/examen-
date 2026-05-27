from app.extensions import db

class Cliente(db.Model):

    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))

    pedidos = db.relationship("Pedido", backref="cliente", lazy=True)