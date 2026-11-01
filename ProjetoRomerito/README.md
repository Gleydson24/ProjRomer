# Gerenciador de Jogos

Projeto desenvolvido em Python com Flask e Flask-SQLAlchemy para cadastrar categorias, jogos e jogadores, além de relacionar jogadores aos jogos.

## Requisitos

- Python 3 instalado
- pip

## Instalação

1. Abra o terminal na pasta do projeto.
2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:

   **Windows (PowerShell):**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   **Linux ou macOS:**
   ```bash
   source venv/bin/activate
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Como executar

Na pasta onde está o arquivo `app.py`, execute:

```bash
python app.py
```

Depois, abra no navegador o endereço indicado no terminal, normalmente `http://127.0.0.1:5000`.

O banco SQLite `sistema_jogos.db` é criado automaticamente quando a aplicação é iniciada.

Para inserir os dados iniciais de categorias e jogos, execute:

```bash
python seed.py
```

## Funcionalidades

- Cadastro, listagem, edição e exclusão de categorias.
- Cadastro, listagem, edição, detalhes e exclusão de jogos.
- Cadastro, listagem, edição, perfil e exclusão de jogadores.
- Relacionamento muitos-para-muitos (N:N) entre jogadores e jogos.
- Na página de perfil do jogador é possível visualizar, adicionar e remover jogos da conta.

## Estrutura do projeto

- `app.py`: inicialização da aplicação e registro das rotas.
- `database.py`: configuração da instância do SQLAlchemy.
- `models/`: entidades do banco de dados.
- `controllers/`: rotas e operações da aplicação.
- `templates/`: páginas HTML.
- `seed.py`: cadastro de dados iniciais.
- `DIARIO.md`: registro das atividades do grupo.

## Autoria e responsabilidades

- **Gleydson:** inicialização da aplicação, configuração do banco de dados e parte de categorias; também participou da estrutura compartilhada da interface.
- **Derickson:** entidade Jogo, tabela de associação N:N, operações de vínculo pelo lado do jogo, páginas de jogos e dados iniciais.
- **Athos:** entidade Jogador, operações CRUD de jogadores, páginas de jogadores, gerenciamento dos jogos vinculados ao jogador e documentação do projeto.

## Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- Bootstrap
