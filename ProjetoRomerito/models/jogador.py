from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import db
from models.jogo import jogador_jogo


class Jogador(db.Model):
    __tablename__ = "jogadores"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nickname: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)

    jogos = relationship(
        "Jogo",
        secondary=jogador_jogo,
        back_populates="jogadores",
    )
from database import db


class Jogador(db.Model):
    __tablename__ = 'jogadores'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    jogos = db.relationship(
        'Jogo',
        secondary='jogador_jogo',
        back_populates='jogadores'
    )
from database import db
from models.jogo import jogador_jogo


class Jogador(db.Model):
    __tablename__ = 'jogador'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    jogos = db.relationship('Jogo', secondary=jogador_jogo, back_populates='jogadores')