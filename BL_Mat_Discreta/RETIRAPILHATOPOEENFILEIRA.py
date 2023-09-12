from collections import deque

def desempilha(fila: deque, pilha: []):
    for i in range(len(pilha)):
        fila.append(pilha.pop(0))
        
pilha = ['21 - Rio de Janeiro', '11 - São paulo', '31 - Minas Gerais', '91 - Belém', '27 - Vitória', '71 - Salvador']
fila = deque()

print(f'Pilha: {pilha}')

desempilha(fila, pilha)
    
print(f'Pilha: {pilha}')
print(f'Fila: {fila}')