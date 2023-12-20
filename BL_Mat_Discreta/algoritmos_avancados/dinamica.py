def troco_dinamico(valor, moedas):
    tabela = [float('inf')] * (valor + 1)
    tabela[0] = 0
    
    for i in range(1, valor + 1):
        for moeda in moedas:
            if i - moeda >= 0:
                tabela[i] = min(tabela[i], tabela[i - moeda] + 1)
    
    troco = []
    while valor > 0:
        for moeda in moedas:
            if valor - moeda >= 0 and tabela[valor] == tabela[valor - moeda] + 1:
                troco.append(moeda)
                valor -= moeda
                break
    
    return troco

valor = 37
moedas = [1, 5, 10, 25, 50]
troco_dinamico_resultado = troco_dinamico(valor, moedas)

print(f'Troco Dinâmico: {troco_dinamico_resultado}')
