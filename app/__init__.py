from flask import Flask
from app.config import Config
from app.extensions import db, migrate

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # importar modelos
    from app.models import Producto, Cliente, Pedido

    # blueprints
    from app.blueprints.productos import bp_productos
    from app.blueprints.clientes import bp_clientes
    from app.blueprints.pedidos import bp_pedidos

    app.register_blueprint(bp_productos, url_prefix="/productos")
    app.register_blueprint(bp_clientes, url_prefix="/clientes")
    app.register_blueprint(bp_pedidos, url_prefix="/pedidos")

    return app