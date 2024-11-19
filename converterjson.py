import json

# Abrir e ler o arquivo enviado
with open("pokemonmoves.txt", "r") as file:
    lines = file.readlines()

# Lista para armazenar os movimentos
movements = []

# Processar cada linha do arquivo
for line in lines:
    parts = line.strip().split("\t")  # Dividir por tabulação
    if len(parts) >= 6:  # Certificar que a linha está no formato esperado
        movement = {
            "name": parts[0],
            "type": parts[1],
            "category": parts[2],
            "power": parts[3] if parts[3] != "—" else None,
            "accuracy": parts[4] if parts[4] != "—" else None,
            "pp": parts[5],
            "description": parts[6] if len(parts) > 6 else None,
        }
        movements.append(movement)

# Salvar os movimentos em um arquivo JSON
with open("movements.json", "w") as json_file:
    json.dump(movements, json_file, indent=4)

print("Movimentos convertidos para JSON com sucesso!")
