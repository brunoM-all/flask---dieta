# app.py
from flask import Flask
from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa o db com a aplicação
db.init_app(app)

# Importa e registra o blueprint das rotas (faça isso depois de inicializar o db)
from routes import bp_refeicoes
app.register_blueprint(bp_refeicoes)

# Rota simples para teste
@app.route('/teste')
def teste():
    return "Teste OK!"

if __name__ == '__main__':
    with app.app_context():
        # Opcional: se desejar criar as tabelas automaticamente ao iniciar
        db.create_all()
    print("Mapa de URLs:")
    print(app.url_map)
    app.run(debug=True)
