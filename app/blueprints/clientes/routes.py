from app.blueprints.clientes import bp_clientes

@bp_clientes.route("/")
def index():
    return "Clientes OK"