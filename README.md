# pokemon_database_project2
Projeto feito por Giuseppe Filippo Camardella Barbosa RA:22121068-5.

Modelo Relacional
![image](https://github.com/user-attachments/assets/ca3843ea-dd56-4dca-af0d-c527f8dc24fd)

![image](https://github.com/user-attachments/assets/2bf94039-320d-46a1-a260-87203eafcc1a)

Um pokemon é um ser fictício do jogo pokémon que interage em batalhas contra outros pokemons cada um tendo uma habilidade única e um set de 4 movimentos

Para utilizar o código
- Criar a conexão com o PostgreSQL.
- Configurar tabelas para Pokémon, movimentos e relações no banco.
- Inserir os dados no banco de dados.
Ultilizando o código consegue criar a conexão com o PostgresSQL, mas ainda precisa mandar as seguintes queries:

CREATE TABLE IF NOT EXISTS pokemons (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    tipo1 VARCHAR(20),
    tipo2 VARCHAR(20),
    habilidade VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS movimentos (
    name VARCHAR(50) PRIMARY KEY,
    type VARCHAR(20),
    category VARCHAR(20),
    power VARCHAR(10),
    accuracy VARCHAR(10),
    pp VARCHAR(10),
    description TEXT
);

CREATE TABLE IF NOT EXISTS pokemon_movimentos (
    pokemon_id INT REFERENCES pokemons(id) ON DELETE CASCADE,
    movimento_nome VARCHAR(50) REFERENCES movimentos(name) ON DELETE CASCADE,
    PRIMARY KEY (pokemon_id, movimento_nome)
);
