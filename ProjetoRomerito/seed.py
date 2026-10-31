
from app import create_app
from database import db
from models.categoria import Categoria
from models.jogo import Jogo


def seed():
    app = create_app()

    with app.app_context():

        categorias = [
            {"nome": "Ação", "descricao": "Jogos de ação"},
            {"nome": "RPG", "descricao": "Jogos de RPG"},
            {"nome": "Esportes", "descricao": "Jogos esportivos"},
            {"nome": "Estratégia", "descricao": "Jogos de estratégia"}
        ]

        for dados in categorias:
            categoria = Categoria.query.filter_by(nome=dados["nome"]).first()

            if categoria is None:
                db.session.add(Categoria(**dados))

        db.session.commit()

        jogos = [
            {
                "titulo": "Minecraft",
                "genero": "Sandbox",
                "preco": 99.90,
                "categoria": "Ação"
            },
            {
                "titulo": "Stardew Valley",
                "genero": "Simulação",
                "preco": 24.99,
                "categoria": "RPG"
            },
            {
                "titulo": "FIFA 24",
                "genero": "Esportes",
                "preco": 199.90,
                "categoria": "Esportes"
            },
            {
                "titulo": "Civilization VI",
                "genero": "Estratégia",
                "preco": 129.90,
                "categoria": "Estratégia"
            }
        ]

        for dados in jogos:
            jogo_existente = Jogo.query.filter_by(
                titulo=dados["titulo"]
            ).first()

            if jogo_existente is None:
                categoria = Categoria.query.filter_by(
                    nome=dados["categoria"]
                ).first()

                novo_jogo = Jogo(
                    titulo=dados["titulo"],
                    genero=dados["genero"],
                    preco=dados["preco"],
                    categoria_id=categoria.id
                )

                db.session.add(novo_jogo)

        db.session.commit()

        print("Dados iniciais cadastrados com sucesso!")


if __name__ == "__main__":
    seed()
