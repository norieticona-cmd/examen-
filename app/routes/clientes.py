from flask import Blueprint, render_template, request, redirect, url_for
from app.extensions import db

# Forzamos la creación del objeto que Flask está buscando desesperadamente
bp_clientes = Blueprint('clientes', __name__)

# Importación interna para evitar cualquier cruce de cables
from app.models.cliente import Cliente

@bp_clientes.route('/')
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes/lista.html', clientes=clientes)

@bp_clientes.route('/nuevo', methods=['GET', 'POST'])
def crear_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        nuevo_cliente = Cliente(nombre=nombre, telefono=telefono)
        db.session.add(nuevo_cliente)
        db.session.commit()
        return redirect(url_for('clientes.listar_clientes'))
    return render_template('clientes/formulario.html', cliente=None)

@bp_clientes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.telefono = request.form['telefono']
        db.session.commit()
        return redirect(url_for('clientes.listar_clientes'))
    return render_template('clientes/formulario.html', cliente=cliente)

@bp_clientes.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes.listar_clientes'))