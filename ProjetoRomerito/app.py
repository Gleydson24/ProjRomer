import os
from flask import Flask, redirect, url_for
from database import db

from models.jogo import Jogo, jogador_jogo
from models.jogador import Jogador

from controllers.categoria_controller import categoria_bp
from controllers.jogo_controller import jogo_bp
from controllers.jogador_controller import jogador_bp


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'PowerRangerSenha'
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sistema_jogos.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(categoria_bp, url_prefix='/categorias')
    app.register_blueprint(jogo_bp, url_prefix='/jogos')
    app.register_blueprint(jogador_bp, url_prefix='/jogadores')

    @app.route('/')
    def index():
        return redirect(url_for('jogo.index'))
    
    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)