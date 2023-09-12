from collections import deque

def add_letra(fila, letra):
    fila.append(letra)
    print(f'Adicionando {letra}: {fila}')

def add_letra_inicio(fila, letra):
    fila.appendleft(letra)
    print(f'Adicionando {letra}: {fila}')

def remover_letra(fila):
    if fila:
        letra = fila.popleft()
        print(f'Retirando letra: {letra}')
    else:
        print("Lista vazia!")

fila = deque()

#adicionando letras na fila
add_letra(fila, "A")
add_letra(fila, "B")
add_letra(fila, "C")
add_letra(fila, "D")
add_letra(fila, "E")
add_letra(fila, "F")
add_letra(fila, "G")
print(fila)

remover_letra(fila)

print(f'Retirando último: {fila.pop()}')
print(fila)

#adicionando mais letras na fila
add_letra(fila, "H")
add_letra(fila, "J")
add_letra_inicio(fila, "K")
add_letra_inicio(fila, "L")
print(fila)

#limpando fila
fila.clear()
print(fila)
remover_letra(fila)