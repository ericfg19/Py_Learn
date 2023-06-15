def count_sonar(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    alteracao = 0
    result = f"Sequência de aumento e diminuição do sonar consultando o arquivo >{arquivo}<\n"
    #conta para verificação de profundidade
    for i in range(1, len(linhas)):
        profundidade_atual = int(linhas[i])
        profundidade_anterior = int(linhas[i-1])
        
        if profundidade_atual > profundidade_anterior:
            alteracao += 1
            result += f"{profundidade_atual} (aumentou)\n"
        elif profundidade_atual < profundidade_anterior:
            result += f"{profundidade_atual} (diminuiu)\n"
    print(f"Alterações: {alteracao}")
    return result

# Teste com o arquivo exemplo1.txt
result1 = count_sonar('exemplo1.txt')
print(result1)

# Teste com o arquivo exemplo2.txt
result2 = count_sonar('exemplo2.txt')
print(result2)
