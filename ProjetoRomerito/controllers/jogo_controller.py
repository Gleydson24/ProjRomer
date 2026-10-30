
from flask import Blueprint, render_template, request, redirect, url_for
from database import db
from models.jogo import Jogo
from models.jogador import Jogador
from models.categoria import Categoria

jogo_bp = Blueprint('jogo', __name__)


@jogo_bp.route('/')
def index():
    jogos = Jogo.query.all()
    return render_template('jogo/index.html', jogos=jogos)


@jogo_bp.route('/novo', methods=['GET', 'POST'])
def criar():
    categorias = Categoria.query.all()

    if request.method == 'POST':
        novo_jogo = Jogo(
            titulo=request.form['titulo'],
            genero=request.form['genero'],
            preco=float(request.form['preco']),
            categoria_id=request.form['categoria_id']
        )

        db.session.add(novo_jogo)
        db.session.commit()

        return redirect(url_for('jogo.index'))

    return render_template('jogo/form.html', categorias=categorias)


@jogo_bp.route('/<int:id>')
def detalhes(id):
    jogo = Jogo.query.get_or_404(id)
    return render_template('jogo/detalhes.html', jogo=jogo)


@jogo_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar(id):
    jogo = Jogo.query.get_or_404(id)
    categorias = Categoria.query.all()

    if request.method == 'POST':
        jogo.titulo = request.form['titulo']
        jogo.genero = request.form['genero']
        jogo.preco = float(request.form['preco'])
        jogo.categoria_id = request.form['categoria_id']

        db.session.commit()

        return redirect(url_for('jogo.index'))

    return render_template('jogo/form.html', jogo=jogo, categorias=categorias)


@jogo_bp.route('/<int:id>/excluir', methods=['POST'])
def excluir(id):
    jogo = Jogo.query.get_or_404(id)

    db.session.delete(jogo)
    db.session.commit()

    return redirect(url_for('jogo.index'))


@jogo_bp.route('/<int:id>/jogadores/vincular', methods=['POST'])
def vincular_jogador(id):
    jogo = Jogo.query.get_or_404(id)
    jogador = Jogador.query.get_or_404(request.form['jogador_id'])

    if jogador not in jogo.jogadores:
        jogo.jogadores.append(jogador)
        db.session.commit()

    return redirect(url_for('jogo.detalhes', id=id))


@jogo_bp.route('/<int:id>/jogadores/<int:jogador_id>/desvincular', methods=['POST'])
def desvincular_jogador(id, jogador_id):
    jogo = Jogo.query.get_or_404(id)
    jogador = Jogador.query.get_or_404(jogador_id)

    if jogador in jogo.jogadores:
        jogo.jogadores.remove(jogador)
        db.session.commit()

    return redirect(url_for('jogo.detalhes', id=id))
