import matplotlib.pyplot as plt

import pandas as pd

dados_pib = pd.read_csv('Assessment_PIBs.csv', index_col='País')


ano = []

#### FUNÇÃO PARA SOLICITAR TODAS VARIAÇÕES DE PIB ###
def variacao_pib(dados_pib):
    for pais in list(dados_pib["2020"].index):
        variacao = (dados_pib["2020"][pais] / dados_pib["2013"][pais] - 1) * 100
        print(f"{pais}\t\t Variação de {variacao:.2f} % entre 2013 e 2020.")
####

###### INPUTS

pais = input("Informe um país: ")
ano_pib = input("Informe um ano entre 2013 e 2020: ")
######
if ano_pib in dados_pib :
    if pais in dados_pib[ano_pib]:
        print(f"PIB do {pais} em {ano_pib} foi de R$ {dados_pib[ano_pib][pais]} Trilhões.")
        variacao = (dados_pib["2020"][pais] / dados_pib["2013"][pais] - 1) * 100
        print(f"{pais}\t\t Variação de {variacao:.2f} % entre 2013 e 2020.")
        
        
        ## grafico plt
        eixox = dados_pib.columns
        eixoy = [dados_pib[ano][pais] for ano in dados_pib.columns]

        plt.plot(eixox, eixoy)
        plt.show()
        ##
        
    else:
        print("O país não está disponível.")
        
else:
    print("O ano não está disponível.")