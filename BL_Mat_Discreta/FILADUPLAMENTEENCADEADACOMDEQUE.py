from collections import deque

fila = deque()

fila.append("A")
fila.append("B")
fila.append("C")
fila.append("D")
fila.append("E")
fila.append("F")
fila.append("G")

# Mostra fila
if fila:
    print(f'Fila atual: {fila}\n')
else:
    print("Lista vazia!")

print(f'Retirando: {fila.popleft()}')

# Mostra fila
if fila:
    print(f'Fila atual: {fila}\n')
else:
    print("Lista vazia!")

#fila.append("D")
print(f'Retirando: {fila.popleft()}')
print(f'adicionando E: {fila.append("E")}')
print(f'adicionando F: {fila.append("F")}')
#fila.append("F")

# Mostra fila
if fila:
    print(f'Fila atual: {fila}\n')
else:
    print("Lista vazia!")

# Dando clear na fila
fila.clear()

# Mostra fila
if fila:
    print(f'Fila atual: {fila}\n')
else:
    print("Lista vazia!")