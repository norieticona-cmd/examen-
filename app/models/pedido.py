from app.extensions import db

class Pedido(db.Model):

    __tablename__ = "pedido"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(50))
    monto = db.Column(db.Float)

    producto_id = db.Column(
        db.Integer,
        db.ForeignKey("producto.id"),
        nullable=False
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey("cliente.id"),
        nullable=False
    )