import csv
import json  # Para carregar os movimentos do arquivo JSON
from faker import Faker
import random

fake = Faker()

# Função para criar 151 Pokémon
def gerar_pokemons(n):
    pokemons = []
    for i in range(1, n + 1):
        pokemon = {
            "id": i,
            "nome": f"Pokemon_{i}",
            "tipo1": fake.random_element(["Grass", "Fire", "Water", "Electric", "Rock", "Ground", "Psychic", "Normal"]),
            "tipo2": fake.random_element(["None", "Flying", "Poison", "Fairy", "Ice", "Bug"]),
        }
        pokemons.append(pokemon)
    return pokemons

# Função para associar movimentos a Pokémon
def associar_movimentos(pokemons, movimentos, max_movimentos=4):
    relacoes = []
    for pokemon in pokemons:
        movimentos_escolhidos = random.sample(movimentos, k=random.randint(1, max_movimentos))
        for movimento in movimentos_escolhidos:
            relacoes.append({
                "pokemon_id": pokemon["id"],
                "movimento_nome": movimento["name"]  # Chave adaptada para o JSON
            })
    return relacoes

# Função para salvar dados em CSV
def salvar_csv(dados, colunas, arquivo):
    with open(arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(colunas)
        for dado in dados:
            writer.writerow([dado[coluna] for coluna in colunas])

# Carregar movimentos do arquivo JSON
with open('movements.json', encoding='utf-8') as f:
    movimentos = json.load(f)

# Gerar dados
pokemons = gerar_pokemons(151)
relacoes_pokemon_movimento = associar_movimentos(pokemons, movimentos)

# Salvar dados em CSV
salvar_csv(pokemons, ["id", "nome", "tipo1", "tipo2"], "pokemons.csv")
salvar_csv(movimentos, ["name", "type", "category", "power", "accuracy", "pp", "description"], "movimentos.csv")
salvar_csv(relacoes_pokemon_movimento, ["pokemon_id", "movimento_nome"], "pokemon_movimentos.csv")

print("Dados de Pokémon e movimentos salvos com sucesso em arquivos CSV!")
