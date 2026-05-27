from flask import Blueprint, render_template, request, redirect, url_for
from app.models.pedido import Pedido
from app.models.cliente import Cliente
from app.models.producto import Producto
from app.extensions import db

bp_pedidos = Blueprint('pedidos', __name__)

@bp_pedidos.route('/')
def listar_pedidos():
    pedidos = Pedido.query.all()
    return render_template('pedidos/lista.html', pedidos=pedidos)

@bp_pedidos.route('/nuevo', methods=['GET', 'POST'])
def crear_pedido():
    if request.method == 'POST':
        cliente_id = int(request.form['cliente_id'])
        producto_id = int(request.form['producto_id'])
        
        # Obtenemos el producto para calcular el monto automáticamente
        producto = Producto.query.get_or_404(producto_id)
        monto = producto.precio # Asumimos cantidad = 1 para simplificar el requerimiento
        
        nuevo_pedido = Pedido(cliente_id=cliente_id, producto_id=producto_id, monto=monto)
        
        # Descontar del stock como lógica de negocio
        if producto.stock > 0:
            producto.stock -= 1
            db.session.add(nuevo_pedido)
            db.session.commit()
            
        return redirect(url_for('pedidos.listar_pedidos'))
        
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    return render_template('pedidos/crear.html', clientes=clientes, productos=productos)