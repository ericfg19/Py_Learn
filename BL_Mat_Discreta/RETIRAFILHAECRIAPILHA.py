from collections import deque
    
# retira o primeiro da fila e adiciona na pilha
def empilha(fila: deque, pilha: []):
    for i in range(len(fila)):
        pilha.append(fila.popleft())
        

fila = deque(['11', '22', '33', '44', '66', '55', '77'])
pilha = []

print(f'Fila: {fila}')

empilha(fila, pilha)

print(f'Fila: {fila}')
print(f'Pilha: {pilha}')




