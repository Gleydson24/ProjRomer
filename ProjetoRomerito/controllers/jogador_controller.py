from flask import Blueprint

jogador_bp = Blueprint('jogador', __name__)


@jogador_bp.route('/')
def index():
    return "Módulo de Jogadores em desenvolvimento"