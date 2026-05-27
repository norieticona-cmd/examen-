from app import create_app

app = create_app()

if __name__ == '__main__':
    # Modo de depuración activado para visualizar cambios en caliente
    app.run(debug=True, port=5000)