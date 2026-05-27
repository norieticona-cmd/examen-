from flask import render_template, request, redirect, url_for
from app.blueprints.clientes import bp_clientes
from app.extensions import db
from app.models import Cliente


@bp_clientes.route("/")
def index():
    clientes = Cliente.query.all()
    return render_template("clientes/index.html", clientes=clientes)


@bp_clientes.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nuevo = Cliente(
            nombre=request.form["nombre"],
            telefono=request.form["telefono"]
        )

        db.session.add(nuevo)
        db.session.commit()

        return redirect(url_for("clientes.index"))

    return render_template("clientes/crear.html")


@bp_clientes.route("/eliminar/<int:id>")
def eliminar(id):
    cliente = Cliente.query.get_or_404(id)

    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for("clientes.index"))