⚡ Projeto Pokémon Database ⚡
Criado por Giuseppe Filippo Camardella Barbosa
RA: 22121068-5

🐾 Descrição do Projeto
Este projeto tem como objetivo criar um banco de dados para armazenar informações de Pokémon, suas habilidades únicas, e os movimentos que podem realizar em batalhas. Assim como Pikachu, cada Pokémon tem seu próprio estilo e características que o tornam especial!

🧩 Modelo Relacional
Aqui está o modelo relacional usado para estruturar o banco de dados:
⚠ Insira aqui o link ou a imagem do diagrama relacional ⚠

🎮 Sobre os Pokémon
Cada Pokémon é um ser fictício do universo Pokémon.
Eles participam de batalhas, cada um com uma habilidade única e um conjunto de 4 movimentos.
Movimentos podem variar em tipo, poder e categoria (físico, especial ou status).
Assim como Pikachu, alguns Pokémon brilham mais com seus tipos e movimentos! 🌟

⚙️ Instruções de Uso
Para usar este projeto, siga os passos abaixo:

Configurar o Banco de Dados PostgreSQL:

Configure o PostgreSQL no seu ambiente local.
Certifique-se de ter as dependências Python instaladas (psycopg2 ou equivalente).
Criar as Tabelas no Banco de Dados:
Utilize as queries fornecidas abaixo para criar a estrutura inicial.

Executar o Código:
Use o script em Python para popular o banco com dados fictícios de Pokémon e movimentos.

📜 Queries para Criar as Tabelas
Pokémon Table
sql
Copiar código
CREATE TABLE IF NOT EXISTS pokemons (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    tipo1 VARCHAR(20),
    tipo2 VARCHAR(20),
    habilidade VARCHAR(50)
);
Movimentos Table
sql
Copiar código
CREATE TABLE IF NOT EXISTS movimentos (
    name VARCHAR(50) PRIMARY KEY,
    type VARCHAR(20),
    category VARCHAR(20),
    power VARCHAR(10),
    accuracy VARCHAR(10),
    pp VARCHAR(10),
    description TEXT
);
Relação Pokémon-Movimentos
sql
Copiar código
CREATE TABLE IF NOT EXISTS pokemon_movimentos (
    pokemon_id INT REFERENCES pokemons(id) ON DELETE CASCADE,
    movimento_nome VARCHAR(50) REFERENCES movimentos(name) ON DELETE CASCADE,
    PRIMARY KEY (pokemon_id, movimento_nome)
);
✨ Consultas Interessantes
Assim como Pikachu tem sua Thunderbolt ⚡, explore as habilidades dos Pokémon no banco com estas queries:

1. Pokémon do tipo "Psíquico"
sql
Copiar código
SELECT * 
FROM pokemons 
WHERE tipo1 = 'Psychic' OR tipo2 = 'Psychic';
2. Pokémon com o movimento "Blizzard"
sql
Copiar código
SELECT p.*
FROM pokemons p
JOIN pokemon_movimentos pm ON p.id = pm.pokemon_id
WHERE pm.movimento_nome = 'Blizzard';
3. Movimentos do tipo "Grama"
sql
Copiar código
SELECT * 
FROM movimentos 
WHERE type = 'Grass';
4. Pokémon do tipo "Fantasma"
sql
Copiar código
SELECT * 
FROM pokemons 
WHERE tipo1 = 'Ghost' OR tipo2 = 'Ghost';
5. Pokémon com dois tipos
sql
Copiar código
SELECT * 
FROM pokemons 
WHERE tipo2 != 'None';
6. Pokémon com movimento de categoria "Especial"
sql
Copiar código
SELECT DISTINCT p.*
FROM pokemons p
JOIN pokemon_movimentos pm ON p.id = pm.pokemon_id
JOIN movimentos m ON pm.movimento_nome = m.name
WHERE m.category = 'Special';
7. Pokémon que possuem movimentos com mais de 50 de poder
sql
Copiar código
SELECT DISTINCT p.*
FROM pokemons p
JOIN pokemon_movimentos pm ON p.id = pm.pokemon_id
JOIN movimentos m ON pm.movimento_nome = m.name
WHERE CAST(m.power AS INTEGER) > 50;
8. Movimentos com precisão menor que 90
sql
Copiar código
SELECT * 
FROM movimentos 
WHERE CAST(accuracy AS INTEGER) < 90;
9. Pokémon com movimentos do tipo "Fogo"
sql
Copiar código
SELECT DISTINCT p.*
FROM pokemons p
JOIN pokemon_movimentos pm ON p.id = pm.pokemon_id
JOIN movimentos m ON pm.movimento_nome = m.name
WHERE m.type = 'Fire';
10. Pokémon com mais de 3 movimentos associados
sql
Copiar código
SELECT p.*, COUNT(pm.movimento_nome) as total_movimentos
FROM pokemons p
JOIN pokemon_movimentos pm ON p.id = pm.pokemon_id
GROUP BY p.id
HAVING COUNT(pm.movimento_nome) > 3;
🌟 Coloque seu Pikachu para brilhar!
Configure o banco de dados, rode o código, e explore o universo Pokémon com queries mágicas e temáticas. Lembre-se: ser um Mestre Pokémon exige prática e estratégia!

⚡ Gotta catch 'em all! ⚡
