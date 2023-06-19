name_file = "conjuntos.txt"
conjuntos = []

try:
  with open(name_file, 'r') as arq:
    for linha in arq:
      conjunto = set(map(int, linha.split()))
      conjuntos.append(conjunto)
except FileNotFoundError:
  print("Arquivo não encontrado.")
except ValueError:
  print("Erro na conversão dos elementos para inteiros.")

if len(conjuntos) == 0:
  intersecao = set()
else:
  intersecao = set.intersection(*conjuntos)

num_elementos = len(intersecao)

print("Resultado da interseção:", intersecao)
print("Número de elementos na interseção:", num_elementos)