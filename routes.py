# routes.py
from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Refeicao
from extensions import db

bp_refeicoes = Blueprint('refeicoes', __name__, url_prefix='/refeicoes')

@bp_refeicoes.route('', methods=['POST'])
def criar_refeicao():
    dados = request.get_json()
    try:
        nova_refeicao = Refeicao(
            nome=dados['nome'],
            descricao=dados.get('descricao'),
            data_hora=datetime.fromisoformat(dados['data_hora']),
            dentro_dieta=dados['dentro_dieta']
        )
        db.session.add(nova_refeicao)
        db.session.commit()
        return jsonify({'mensagem': 'Refeição criada com sucesso!'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

@bp_refeicoes.route('', methods=['GET'])
def listar_refeicoes():
    refeicoes = Refeicao.query.all()
    resultado = [{
        'id': r.id,
        'nome': r.nome,
        'descricao': r.descricao,
        'data_hora': r.data_hora.isoformat(),
        'dentro_dieta': r.dentro_dieta
    } for r in refeicoes]
    return jsonify(resultado), 200

@bp_refeicoes.route('/<int:id>', methods=['GET'])
def obter_refeicao(id):
    refeicao = Refeicao.query.get_or_404(id)
    resultado = {
        'id': refeicao.id,
        'nome': refeicao.nome,
        'descricao': refeicao.descricao,
        'data_hora': refeicao.data_hora.isoformat(),
        'dentro_dieta': refeicao.dentro_dieta
    }
    return jsonify(resultado), 200

@bp_refeicoes.route('/<int:id>', methods=['PUT'])
def atualizar_refeicao(id):
    refeicao = Refeicao.query.get_or_404(id)
    dados = request.get_json()
    try:
        refeicao.nome = dados.get('nome', refeicao.nome)
        refeicao.descricao = dados.get('descricao', refeicao.descricao)
        if 'data_hora' in dados:
            refeicao.data_hora = datetime.fromisoformat(dados['data_hora'])
        if 'dentro_dieta' in dados:
            refeicao.dentro_dieta = dados['dentro_dieta']
        db.session.commit()
        return jsonify({'mensagem': 'Refeição atualizada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

@bp_refeicoes.route('/<int:id>', methods=['DELETE'])
def deletar_refeicao(id):
    refeicao = Refeicao.query.get_or_404(id)
    db.session.delete(refeicao)
    db.session.commit()
    return jsonify({'mensagem': 'Refeição removida com sucesso!'}), 200

print("Rotas do blueprint registradas!")
