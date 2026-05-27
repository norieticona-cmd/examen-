from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.producto import Producto
from app.extensions import db

bp_productos = Blueprint('productos', __name__)

@bp_productos.route('/')
def listar_productos():
    productos = Producto.query.all()
    return render_template('productos/lista.html', productos=productos)

@bp_productos.route('/nuevo', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])
        
        nuevo_prod = Producto(nombre=nombre, precio=precio, stock=stock)
        db.session.add(nuevo_prod)
        db.session.commit()
        return redirect(url_for('productos.listar_productos'))
    return render_template('productos/formulario.html', producto=None)

@bp_productos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.precio = float(request.form['precio'])
        producto.stock = int(request.form['stock'])
        db.session.commit()
        return redirect(url_for('productos.listar_productos'))
    return render_template('productos/formulario.html', producto=producto)

@bp_productos.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('productos.listar_productos'))