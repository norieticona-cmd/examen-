from flask import render_template, request, redirect, url_for
from app.blueprints.pedidos import bp_pedidos
from app.extensions import db
from app.models import Pedido, Cliente, Producto


@bp_pedidos.route("/")
def index():
    pedidos = Pedido.query.all()
    return render_template("pedidos/index.html", pedidos=pedidos)


@bp_pedidos.route("/crear", methods=["GET", "POST"])
def crear():
    clientes = Cliente.query.all()
    productos = Producto.query.all()

    if request.method == "POST":

        producto = Producto.query.get(request.form["producto_id"])
        cliente = Cliente.query.get(request.form["cliente_id"])

        nuevo = Pedido(
            fecha=request.form["fecha"],
            monto=float(request.form["monto"]),
            producto_id=producto.id,
            cliente_id=cliente.id
        )

        db.session.add(nuevo)
        db.session.commit()

        return redirect(url_for("pedidos.index"))

    return render_template(
        "pedidos/crear.html",
        clientes=clientes,
        productos=productos
    )