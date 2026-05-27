from flask import Flask
from app.extensions import db, migrate
from app.config import Config

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # 🔥 IMPORTAR MODELOS
    from app.models import Producto, Cliente, Pedido

    # 🔥 IMPORTAR BLUEPRINTS
    from app.blueprints.productos import bp_productos
    from app.blueprints.clientes import bp_clientes
    from app.blueprints.pedidos import bp_pedidos

    # 🔥 REGISTRAR BLUEPRINTS (ESTO ES CLAVE)
    app.register_blueprint(bp_productos, url_prefix="/productos")
    app.register_blueprint(bp_clientes, url_prefix="/clientes")
    app.register_blueprint(bp_pedidos, url_prefix="/pedidos")

    from flask import render_template

    @app.route("/")
    def home():
        return render_template("index.html")
    return app