import matplotlib.pyplot as plt

def extrair_dados(caminho_arquivo):
    arquivo = open(caminho_arquivo)
    conteudo = arquivo.read()
    arquivo.close()
    
    conteudo = conteudo.splitlines()
    rotulos = conteudo[0]
    rotulos = rotulos.split(',')
    conteudo = conteudo[1:]
    
    print(rotulos)
    print(conteudo)
    dados = []
    for elemento in conteudo:
        elemento = elemento.splitlines()
        dados.append(elemento)
    
    return rotulos, dados
    
rotulos, dados = extrair_dados('kobe.csv')

def calcular_pontos(temporada):
    rotulos, dados = extrair_dados('kobe.csv')
    indice_temp = rotulos.index('TEMPORADA')
    indice_pontos = rotulos.index('PONTOS')
    indice_partidas = rotulos.index('PARTIDAS')
    
    for elemento in dados:
        if int(elemento[indice_temp]) == temporada:
            media_pontos = float(elemento[indice_pontos])
            num_partidas = int(elemento[indice_partidas])
            total_pontos = int(media_pontos * num_partidas)
            
def exibir_grafico(x,y):
    plt.plot(x,y)
    plt.show()
    
def exibir_grafico_percentual_pontos():
    rotulos, dados = extrair_dados('kobe.csv')
    percent_cestas = rotulos.index('%CESTAS')
    temporada = rotulos.index('TEMPORADA')
    
    lista_temporadas = [] # eixo x do grafico
    lista_percent_cestas = [] # eixo y do grafico
    
    
    for elemento in dados:
        lista_temporadas.append(int(elemento[temporada]))
        lista_percent_cestas.append(float(elemento[percent_cestas]))
        
    print(lista_temporadas)
    print(lista_percent_cestas)