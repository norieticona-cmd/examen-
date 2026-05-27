from flask import render_template, request, redirect, url_for
from app.blueprints.productos import bp_productos
from app.extensions import db
from app.models import Producto


@bp_productos.route("/")
def index():
    productos = Producto.query.all()
    return render_template("productos/index.html", productos=productos)

@bp_productos.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nuevo = Producto(
            nombre=request.form["nombre"],
            precio=request.form["precio"],
            stock=request.form["stock"]
        )

        db.session.add(nuevo)
        db.session.commit()

        return redirect(url_for("productos.index"))

    return render_template("productos/crear.html")
@bp_productos.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    producto = Producto.query.get_or_404(id)

    if request.method == "POST":
        producto.nombre = request.form["nombre"]
        producto.precio = request.form["precio"]
        producto.stock = request.form["stock"]

        db.session.commit()
        return redirect(url_for("productos.index"))

    return render_template("productos/editar.html", producto=producto)

@bp_productos.route("/eliminar/<int:id>")
def eliminar(id):
    producto = Producto.query.get_or_404(id)

    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for("productos.index"))