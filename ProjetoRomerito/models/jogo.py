from sqlalchemy import String, Float, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import db

jogador_jogo = Table(
    "jogador_jogo",
    db.metadata,
    Column("jogador_id", ForeignKey("jogadores.id"), primary_key=True),
    Column("jogo_id", ForeignKey("jogos.id"), primary_key=True),
)


class Jogo(db.Model):
    __tablename__ = "jogos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(30), nullable=False)
    genero: Mapped[str] = mapped_column(String(30), nullable=False)
    preco: Mapped[float] = mapped_column(Float, nullable=False)

    categoria_id: Mapped[int] = mapped_column(
        ForeignKey("categorias.id"),
        nullable=False,
    )

    jogadores = relationship(
        "Jogador",
        secondary=jogador_jogo,
        back_populates="jogos",
    )
