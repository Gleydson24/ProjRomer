from database import db

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    jogos = db.relationship('Jogo', backref='categoria', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Categoria {self.nome}>'