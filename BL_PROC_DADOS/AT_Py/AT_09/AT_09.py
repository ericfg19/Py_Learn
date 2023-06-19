import json

with open("clientes.json", 'r') as file:
    clientes = json.load(file)

idades = {"M": [], "F": [], "null": []}

for cliente in clientes:
    idade = cliente['idade']
    genero = cliente['genero']

    if genero in idades:
        idades[genero].append(idade)

idades_min = {}
idades_max = {}
idades_avg = {}

for genero, lista_idades in idades.items():
    if lista_idades:
        idades_min[genero] = min(lista_idades)
        idades_max[genero] = max(lista_idades)
        idades_avg[genero] = sum(lista_idades) / len(lista_idades)
    else:
        idades_min[genero] = None
        idades_max[genero] = None
        idades_avg[genero] = None

print("Idades mínimas:")
for genero, idade_min in idades_min.items():
    if genero == "null":
        genero_texto = "N"
    else:
        genero_texto = genero
    print(f"Gênero {genero_texto}: {idade_min}" if idade_min is not None else f"Gênero {genero_texto}: {idade_min}")

print("Idades máximas:")
for genero, idade_max in idades_max.items():
    if genero == "null":
        genero_texto = "N"
    else:
        genero_texto = genero
    print(f"Gênero {genero_texto}: {idade_max}" if idade_max is not None else f"Gênero {genero_texto}: {idade_max}")

print("Idades médias:")
for genero, idade_avg in idades_avg.items():
    if genero == "null":
        genero_texto = "N"
    else:
        genero_texto = genero
    print(f"Gênero {genero_texto}: {idade_avg:.1f}" if idade_avg is not None else f"Gênero {genero_texto}: {idade_avg}")
