from flask import Blueprint

bp_pedidos = Blueprint(
    "pedidos",
    __name__
)

from app.blueprints.pedidos import routes