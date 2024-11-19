import psycopg2
import json
from faker import Faker
import random

fake = Faker()

# Configurações do banco de dados
DB_CONFIG = {
    'dbname': 'cascalitos',
    'user': 'usuário_teste',
    'password': 'senha_teste',
    'host': 'localhost',
    'port': 5432
}

# Função para criar 151 Pokémon
def gerar_pokemons(n):
    habilidades_disponiveis = [
        "Overgrow", "Blaze", "Torrent", "Shield Dust", "Run Away", "Inner Focus", "Static", "Levitate", "Swift Swim",
        "Chlorophyll", "Flash Fire", "Synchronize", "Intimidate", "Sturdy", "Huge Power", "Volt Absorb", "Pressure"
    ]
    habilidades_usadas = set()

    pokemons = []
    for i in range(1, n + 1):
        habilidade = random.choice(habilidades_disponiveis)
        while habilidade in habilidades_usadas:
            habilidade = random.choice(habilidades_disponiveis)
        habilidades_usadas.add(habilidade)

        tipo1 = fake.random_element(["Grass", "Fire", "Water", "Electric", "Rock", "Ground", "Psychic", "Normal"])
        tipo2 = (
            fake.random_element(["None", "Flying", "Poison", "Fairy", "Ice", "Bug"])
            if random.random() < 0.5
            else "None"
        )

        pokemon = {
            "id": i,
            "nome": fake.first_name(),
            "tipo1": tipo1,
            "tipo2": tipo2,
            "habilidade": habilidade
        }
        pokemons.append(pokemon)
    return pokemons

# Função para associar movimentos
def associar_movimentos(pokemons, movimentos):
    relacoes = []
    for pokemon in pokemons:
        movimentos_escolhidos = random.sample(movimentos, k=4)
        for movimento in movimentos_escolhidos:
            relacoes.append({
                "pokemon_id": pokemon["id"],
                "movimento_nome": movimento["name"]
            })
    return relacoes

# Função para salvar no PostgreSQL
def salvar_no_postgres(conn, pokemons, movimentos, relacoes):
    with conn.cursor() as cursor:
        # Inserir Pokémons
        cursor.executemany("""
            INSERT INTO pokemons (id, nome, tipo1, tipo2, habilidade)
            VALUES (%(id)s, %(nome)s, %(tipo1)s, %(tipo2)s, %(habilidade)s)
        """, pokemons)

        # Inserir movimentos
        cursor.executemany("""
            INSERT INTO movimentos (name, type, category, power, accuracy, pp, description)
            VALUES (%(name)s, %(type)s, %(category)s, %(power)s, %(accuracy)s, %(pp)s, %(description)s)
        """, movimentos)

        # Inserir relações Pokémon-Movimento
        cursor.executemany("""
            INSERT INTO pokemon_movimentos (pokemon_id, movimento_nome)
            VALUES (%(pokemon_id)s, %(movimento_nome)s)
        """, relacoes)

        conn.commit()

# Principal
def main():
    # Conectar ao banco de dados
    conn = psycopg2.connect(**DB_CONFIG)

    # Criar tabelas (caso ainda não existam)
    with conn.cursor() as cursor:
        cursor.execute("""
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
                pokemon_id INT REFERENCES pokemons(id),
                movimento_nome VARCHAR(50) REFERENCES movimentos(name)
            );
        """)
        conn.commit()

    # Carregar movimentos do arquivo JSON
    with open('movements.json', encoding='utf-8') as f:
        movimentos = json.load(f)

    # Gerar dados
    pokemons = gerar_pokemons(151)
    relacoes = associar_movimentos(pokemons, movimentos)

    # Salvar no banco
    salvar_no_postgres(conn, pokemons, movimentos, relacoes)
    print("Dados inseridos no PostgreSQL com sucesso!")

    conn.close()

if __name__ == "__main__":
    main()
