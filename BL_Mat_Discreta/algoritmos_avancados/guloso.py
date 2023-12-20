def troco_guloso(valor, moedas):
    moedas.sort(reverse=True)
    troco = []
    
    for moeda in moedas:
        while valor >= moeda:
            troco.append(moeda)
            valor -= moeda
    
    return troco

def troco_recursivo(valor, moedas):
    if valor == 0:
        return []
    
    moedas.sort(reverse=True)
    
    melhor_troco = None
    melhor_num_moedas = float('inf')
    
    for moeda in moedas:
        if valor >= moeda:
            troco_atual = [moeda] + troco_recursivo(valor - moeda, moedas)
            num_moedas_atual = len(troco_atual)
            
            if num_moedas_atual < melhor_num_moedas:
                melhor_troco = troco_atual
                melhor_num_moedas = num_moedas_atual
    
    return melhor_troco

valor = 37
moedas = [1, 5, 10, 25, 50]
troco_guloso_resultado = troco_guloso(valor, moedas)
troco_recursivo_resultado = troco_recursivo(valor, moedas)

print(f'Troco Guloso: {troco_guloso_resultado}')
print(f'Troco Recursivo: {troco_recursivo_resultado}')
