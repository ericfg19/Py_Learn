def calc_posicao(arquivo):
  posicao_horizontal = 0
  profundidade = 0

  with open(arquivo, 'r') as f:
        for linha in f:
            comando, valor = linha.strip().split()
            valor = int(valor)
            if comando == 'frente':
                posicao_horizontal += valor
            elif comando == 'baixo':
                profundidade += valor
            elif comando == 'cima':
                profundidade -= valor

  return posicao_horizontal, profundidade

arquivo = 'exemplo1.txt'
posicao_horizontal, profundidade = calc_posicao(arquivo)
print(f'Dados do {arquivo}:\n')
print(f'Cálculo de posição horizontal = {posicao_horizontal}')
print(f'Cálculo de rofundidade = {profundidade}')

arquivo = 'exemplo2.txt'
posicao_horizontal, profundidade = calc_posicao(arquivo)
print(f'\nDados do {arquivo}:\n')
print(f'Cálculo de posição horizontal = {posicao_horizontal}')
print(f'Cálculo de rofundidade = {profundidade}')