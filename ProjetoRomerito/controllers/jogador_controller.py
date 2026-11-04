from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models.jogador import Jogador
from models.jogo import Jogo

jogador_bp = Blueprint('jogador', __name__)

@jogador_bp.route('/')
def index():
    jogadores = Jogador.query.all()
    return render_template('jogador/index.html', jogadores=jogadores)

@jogador_bp.route('/novo', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        email = request.form.get('email')

        if not nickname or not email:
            flash('Preencha todos os campos obrigatórios!', 'danger')
            return render_template('jogador/form.html', jogador=None)

        if Jogador.query.filter_by(email=email).first():
            flash('Este e-mail já está cadastrado!', 'warning')
            return render_template('jogador/form.html', jogador=None)

        novo_jogador = Jogador(nickname=nickname, email=email)
        db.session.add(novo_jogador)
        db.session.commit()

        flash('Jogador cadastrado com sucesso!', 'success')
        return redirect(url_for('jogador.index'))

    return render_template('jogador/form.html', jogador=None)

@jogador_bp.route('/<int:id>/perfil')
def perfil(id):
    jogador = Jogador.query.get_or_404(id)
    jogos_disponiveis = Jogo.query.filter(~Jogo.jogadores.any(id=jogador.id)).all()
    return render_template('jogador/perfil.html', jogador=jogador, jogos_disponiveis=jogos_disponiveis)

@jogador_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar(id):
    jogador = Jogador.query.get_or_404(id)

    if request.method == 'POST':
        nickname = request.form.get('nickname')
        email = request.form.get('email')

        if not nickname or not email:
            flash('Preencha todos os campos!', 'danger')
            return render_template('jogador/form.html', jogador=jogador)

        jogador.nickname = nickname
        jogador.email = email

        db.session.commit()
        flash('Dados do jogador atualizados!', 'success')
        return redirect(url_for('jogador.index'))

    return render_template('jogador/form.html', jogador=jogador)

@jogador_bp.route('/<int:id>/excluir', methods=['POST'])
def excluir(id):
    jogador = Jogador.query.get_or_404(id)
    db.session.delete(jogador)
    db.session.commit()
    flash('Jogador removido com sucesso!', 'success')
    return redirect(url_for('jogador.index'))

@jogador_bp.route('/<int:id>/jogos/adicionar', methods=['POST'])
def adicionar_jogo(id):
    jogador = Jogador.query.get_or_404(id)
    jogo_id = request.form.get('jogo_id')
    
    if jogo_id:
        jogo = Jogo.query.get_or_404(jogo_id)
        if jogo not in jogador.jogos:
            jogador.jogos.append(jogo)
            db.session.commit()
            flash(f'Jogo "{jogo.titulo}" adicionado à biblioteca!', 'success')

    return redirect(url_for('jogador.perfil', id=id))

@jogador_bp.route('/<int:id>/jogos/<int:jogo_id>/remover', methods=['POST'])
def remover_jogo(id, jogo_id):
    jogador = Jogador.query.get_or_404(id)
    jogo = Jogo.query.get_or_404(jogo_id)

    if jogo in jogador.jogos:
        jogador.jogos.remove(jogo)
        db.session.commit()
        flash(f'Jogo "{jogo.titulo}" removido da biblioteca!', 'info')

    return redirect(url_for('jogador.perfil', id=id))