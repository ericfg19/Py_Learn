from random import random
import matplotlib.pyplot as plt

class Produto():
    def __init__(self, nome, volume, valor):
        self.nome = nome
        self.volume = volume
        self.valor = valor
        
class Individuo():
    def __init__(self, volumes, valores, teto_volumes, geracao=0):
        self.volumes = volumes
        self.valores = valores
        self.teto_volumes = teto_volumes
        self.avaliacao_nota = 0
        self. volume_ocupado = 0
        self.geracao = geracao
        self.cromossomo = []
        
        for i in range(len(volumes)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
                
    def avaliacao(self):
        nota = 0
        soma_volumes = 0
        for i in range(len(self.cromossomo)):
           if self.cromossomo[i] == '1':
               nota += self.valores[i]
               soma_volumes += self.volumes[i]
        if soma_volumes > self.teto_volumes:
            nota = 1
        self.avaliacao_nota = nota
        self. volume_ocupado = soma_volumes
        
    def crossover(self, outro_individuo):
        corte = round(random()  * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(self.volumes, self.valores, self.teto_volumes, self.geracao + 1),
                  Individuo(self.volumes, self.valores, self.teto_volumes, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos
    
    def mutacao(self, taxa_mutacao):
        #print("Antes %s " % self.cromossomo)
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
        #print("Depois %s " % self.cromossomo)
        return self
        
class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []
        
    def inicializa_populacao(self, volumes, valores, teto_volumes):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(volumes, valores, teto_volumes))
        self.melhor_solucao = self.populacao[0]
        
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.avaliacao_nota,
                                reverse = True)
        
    def melhor_individuo(self, individuo):
        if individuo.avaliacao_nota > self.melhor_solucao.avaliacao_nota:
            self.melhor_solucao = individuo
            
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
           soma += individuo.avaliacao_nota
        return soma
    
    def selec_genitor(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].avaliacao_nota
            pai += 1
            i += 1
        return pai
    
    def visualiza_geracao(self):
        melhor = self.populacao[0]
        print("G:%s -> Valor: %s Volume: %s Cromossomo: %s" % (self.populacao[0].geracao,
                                                               melhor.avaliacao_nota,
                                                               melhor. volume_ocupado,
                                                               melhor.cromossomo))
    
    def processa_alg_genetico(self, taxa_mutacao, quant_geracoes, volumes, valores, teto_volumes):
        self.inicializa_populacao(volumes, valores, teto_volumes)
        
        for individuo in self.populacao:
            individuo.avaliacao()
        
        self.ordena_populacao()
        self.melhor_solucao = self.populacao[0]
        self.lista_solucoes.append(self.melhor_solucao.avaliacao_nota)
        
        self.visualiza_geracao()
        
        for geracao in range(quant_geracoes):
            soma_avaliacao = self.soma_avaliacoes()
            nova_populacao = []
            
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.selec_genitor(soma_avaliacao)
                pai2 = self.selec_genitor(soma_avaliacao)
                
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
            
            self.populacao = list(nova_populacao)
            
            for individuo in self.populacao:
                individuo.avaliacao()
            
            self.ordena_populacao()
            
            self.visualiza_geracao()
            
            melhor = self.populacao[0]
            self.lista_solucoes.append(melhor.avaliacao_nota)
            self.melhor_individuo(melhor)
        
        print("\nMelhor solução -> G: %s Valor: %s Espaço: %s Cromossomo: %s" %
              (self.melhor_solucao.geracao,
               self.melhor_solucao.avaliacao_nota,
               self.melhor_solucao. volume_ocupado,
               self.melhor_solucao.cromossomo))
        
        return self.melhor_solucao.cromossomo
        
        
if __name__ == '__main__':
    #p1 = Produto("Iphone 6", 0.0000899, 2199.12)
    tabela_produtos = []
    tabela_produtos.append(Produto("Refrigerador 1", 1.112, 5999))
    tabela_produtos.append(Produto("Refrigerador 2", 990, 9799))
    tabela_produtos.append(Produto("Iphone 12", 0.0000899, 5999.00))
    tabela_produtos.append(Produto("TV 50' ", 0.420, 1599.00))
    tabela_produtos.append(Produto("TV 60' ", 0.520, 1899.00))
    tabela_produtos.append(Produto("TV 75' ", 0.720, 5599.00))
    tabela_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
    tabela_produtos.append(Produto("Ventilador 1", 0.496, 199.90))
    tabela_produtos.append(Produto("Microondas Electrolux", 0.0650, 459))
    tabela_produtos.append(Produto("Fogao", 0.905, 5999))
    tabela_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
    tabela_produtos.append(Produto("Ventilador 2", 0.950, 390.00))

    volumes = []
    valores = []
    nomes = []
    for produto in tabela_produtos:
        volumes.append(produto.volume)
        valores.append(produto.valor)
        nomes.append(produto.nome)
    limite = 4
    tamanho_populacao = 20
    taxa_mutacao = 0.01
    quant_geracoes = 100
    ag = AlgoritmoGenetico(tamanho_populacao)
    resultado = ag.processa_alg_genetico(taxa_mutacao, quant_geracoes, volumes, valores, limite)
    for i in range(len(tabela_produtos)):
        if resultado[i] == '1':
            print("Nome: %s R$ %s " % (tabela_produtos[i].nome,
                                       tabela_produtos[i].valor))
            
    
    #for valor in ag.lista_solucoes:
    #    print(valor)
    plt.plot(ag.lista_solucoes)
    plt.title("Acompanhamento dos valores")
    plt.show()
    
    