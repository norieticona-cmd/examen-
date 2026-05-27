from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Producto, Cliente, Pedido
from app.extensions import db

bp_productos = Blueprint('productos', __name__)
bp_clientes = Blueprint('clientes', __name__)
bp_pedidos = Blueprint('pedidos', __name__)

# --- CRUD PRODUCTOS ---
@bp_productos.route('/')
def listar_productos():
    return render_template('productos/lista.html', productos=Producto.query.all())

@bp_productos.route('/nuevo', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        p = Producto(nombre=request.form['nombre'], precio=float(request.form['precio']), stock=int(request.form['stock']))
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('productos.listar_productos'))
    return render_template('productos/formulario.html', producto=None)

# --- CRUD CLIENTES ---
@bp_clientes.route('/')
def listar_clientes():
    return render_template('clientes/lista.html', clientes=Cliente.query.all())

@bp_clientes.route('/nuevo', methods=['GET', 'POST'])
def crear_cliente():
    if request.method == 'POST':
        c = Cliente(nombre=request.form['nombre'], telefono=request.form['telefono'])
        db.session.add(c)
        db.session.commit()
        return redirect(url_for('clientes.listar_clientes'))
    return render_template('clientes/formulario.html', cliente=None)

# --- CRUD PEDIDOS ---
@bp_pedidos.route('/')
def listar_pedidos():
    return render_template('pedidos/lista.html', pedidos=Pedido.query.all())

@bp_pedidos.route('/nuevo', methods=['GET', 'POST'])
def crear_pedido():
    if request.method == 'POST':
        prod = Producto.query.get(int(request.form['producto_id']))
        if prod and prod.stock > 0:
            ped = Pedido(cliente_id=int(request.form['cliente_id']), producto_id=prod.id, monto=prod.precio)
            prod.stock -= 1
            db.session.add(ped)
            db.session.commit()
        return redirect(url_for('pedidos.listar_pedidos'))
    return render_template('pedidos/crear.html', clientes=Cliente.query.all(), productos=Producto.query.all())