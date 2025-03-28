# models.py
from extensions import db
from datetime import datetime

class Refeicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    data_hora = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dentro_dieta = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Refeicao {self.nome}>'
