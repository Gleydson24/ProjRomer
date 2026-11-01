from database import db
from models.jogo import jogador_jogo


class Jogador(db.Model):
    __tablename__ = 'jogadores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    jogos = db.relationship(
        'Jogo',
        secondary=jogador_jogo,
        back_populates='jogadores'
    )

    def __repr__(self):
        return f'<Jogador {self.nickname}>'