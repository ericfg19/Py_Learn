import random

# Função para gerar a população inicial
def gera_pop(tamanho_populacao, num_genes):
    return [[random.choice([0, 1]) for _ in range(num_genes)] for _ in range(tamanho_populacao)]

# Função para calcular a aptidão de um indivíduo (soma dos genes)
def calc_aptdao(individuo):
    return sum(individuo)

# Função para ordenar a população com base na aptidão (decrescente)
def ord_pop(populacao):
    return sorted(populacao, key=calc_aptdao, reverse=True)

# Função para realizar a seleção dos indivíduos mais aptos
def selecao(populacao, tamanho_selecionado):
    return populacao[:tamanho_selecionado]

# Função para realizar o crossover entre dois indivíduos
def crossover(individuo1, individuo2):
    ponto_crossover = random.randint(1, len(individuo1) - 1)
    gera_individuo1 = individuo1[:ponto_crossover] + individuo2[ponto_crossover:]
    gera_individuo2 = individuo2[:ponto_crossover] + individuo1[ponto_crossover:]
    return gera_individuo1, gera_individuo2

# Função para realizar a mutação em um indivíduo
def mutacao(individuo, taxa_mutacao):
    if random.random() < taxa_mutacao:  # Probabilidade de mutação
        num_genes_mutacao = random.randint(1, min(3, len(individuo)))
        indices_mutacao = random.sample(range(len(individuo)), num_genes_mutacao)
        for indice in indices_mutacao:
            individuo[indice] = 1 - individuo[indice]
    return individuo

# Números para algoritmo
print("Digite os valores para o cálculo de algoritmo genético\n")
tamanho_populacao_inicial = int(input("Tamanho populacional inicial (sugerido 20):\n"))
tamanho_populacao_cruzamento = int(input("Tamanho populacional inicial (sugerido 30):\n"))
tamanho_populacao_selecao = int(input("Tamanho da população após seleção (sugerido 20):\n"))
num_genes = int(input("Número de Genes (sugerido 6):\n"))  # Função Objetivo - Número de cromossomos.
num_geracoes_max = 1000

# Aumento da taxa de mutação para 5%
taxa_mutacao = 0.05

# Inicialização da população
populacao = gera_pop(tamanho_populacao_inicial, num_genes)

# Iteração sobre as gerações
for geracao in range(num_geracoes_max):
    # Cálculo da aptidão e ordenação da população
    populacao = ord_pop(populacao)
    
    
    melhor_individuo = populacao[0]
    melhor_aptidao = calc_aptdao(melhor_individuo)
    print(f"Geração: {geracao + 1} -> {melhor_aptidao} | {sum(melhor_individuo)} | {melhor_individuo}")
    

    # Verifica se a função objetivo foi atingida
    if melhor_aptidao == num_genes:
        print(f"Função objetivo atingida na geração {geracao + 1}!")
        break
    
    # Seleção dos indivíduos mais aptos
    populacao_selecionada = selecao(populacao, tamanho_populacao_selecao)
    
    # Cruzamento
    nova_populacao = []
    for _ in range(tamanho_populacao_cruzamento // 2):
        pai1, pai2 = random.choices(populacao_selecionada, k=2)
        filho1, filho2 = crossover(pai1, pai2)
        nova_populacao.extend([mutacao(filho1, taxa_mutacao), mutacao(filho2, taxa_mutacao)])
    
    
    # Atualizar a população para a próxima geração
    populacao = nova_populacao
    


    if calc_aptdao(populacao[0]) != num_genes:
        print("Número máximo de gerações atingido. Função objetivo não alcançada.")
