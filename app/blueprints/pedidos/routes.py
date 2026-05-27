from app.blueprints.pedidos import bp_pedidos

@bp_pedidos.route("/")
def index():
    return "Pedidos funcionando"