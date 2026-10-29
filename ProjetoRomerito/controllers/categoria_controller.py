from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models.categoria import Categoria

categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route('/')
def index():
    categorias = Categoria.query.all()
    return render_template('categoria/index.html', categorias=categorias)

@categoria_bp.route('/nova', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')

        if not nome:
            flash('O nome da categoria é obrigatório!', 'danger')
            return render_template('categoria/form.html', categoria=None)

        nova_categoria = Categoria(nome=nome, descricao=descricao)
        db.session.add(nova_categoria)
        db.session.commit()

        flash('Categoria cadastrada com sucesso!', 'success')
        return redirect(url_for('categoria.index'))

    return render_template('categoria/form.html', categoria=None)

@categoria_bp.route('/<int:id>')
def detalhes(id):
    categoria = Categoria.query.get_or_404(id)
    return render_template('categoria/detalhes.html', categoria=categoria)

@categoria_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar(id):
    categoria = Categoria.query.get_or_404(id)

    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')

        if not nome:
            flash('O nome da categoria é obrigatório!', 'danger')
            return render_template('categoria/form.html', categoria=categoria)

        categoria.nome = nome
        categoria.descricao = descricao

        db.session.commit()
        flash('Categoria atualizada com sucesso!', 'success')
        return redirect(url_for('categoria.index'))

    return render_template('categoria/form.html', categoria=categoria)

@categoria_bp.route('/<int:id>/excluir', methods=['POST'])
def excluir(id):
    categoria = Categoria.query.get_or_404(id)
    try:
        db.session.delete(categoria)
        db.session.commit()
        flash('Categoria removida com sucesso!', 'success')
    except Exception:
        db.session.rollback()
        flash('Erro ao excluir a categoria.', 'danger')

    return redirect(url_for('categoria.index'))