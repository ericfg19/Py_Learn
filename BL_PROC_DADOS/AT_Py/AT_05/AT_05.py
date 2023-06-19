import json

with open("clientes.json", 'r') as file:
  clientes = json.load(file)

idade_max = None
idade_min = None

idade_sum = 0
qtd_clientes = len(clientes)

for cliente in clientes:
  idade = cliente['idade']
  if idade_min is None or idade < idade_min:
    idade_min = idade
  if idade_max is None or idade > idade_max:
    idade_max = idade

  idade_sum += idade

idade_avg = idade_sum / qtd_clientes

print(f'Idade Máxima -> {idade_max}')
print(f"Idade Mínima -> {idade_min}")
print(f"Idade Média -> {idade_avg:.1f}")