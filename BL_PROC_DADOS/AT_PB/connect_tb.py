import sqlite3
import pandas as pd
from statistics import mean

cnx = sqlite3.connect('PB_Tabela.db') 

###################################################################################
# 09 +10 - Conectando ao banco, capturando todos os dados e guardando no objeto "iris"
###################################################################################

housingdb = pd.read_sql_query("SELECT * FROM PB_Tabela", cnx)

print("Consulta da tabela - Consumo apresentando o conteúdo das duas variáveis indicadas\n")
# Apresentando o conteúdo do objeto com dados na tela
print(housingdb)


###################################################################################
# 11 + 12 - Apresentando o conteúdo máximo, mínimo e médio + listagem de itens únicos da variável categórica escolhida
###################################################################################

print("\n11 - Consulta da tabela - apresentando os valores máximo, mínimo e a médio dos valores da variável LOT_AREA \n")

housingdb = pd.read_sql_query("SELECT MAX(lot_area) AS Máximo, MIN(lot_area) as Mínimo, AVG(lot_area) as Média  from PB_tabela", cnx)
print(housingdb)


print("\n12 - Consulta da tabela - apresentando uma listagem de itens únicos da variável categórica escolhida - garage_type \n")

housingdb = pd.read_sql_query("SELECT * FROM PB_Tabela WHERE garage_type = 'Detchd'", cnx)
print(housingdb)

###################################################################################
# 13 + 14 - crie uma lista contendo os dados da variável numérica e categórica
###################################################################################

print("\n13 - Consulta da tabela - crie uma lista contendo apenas os dados da variável numérica \n")
# Variável numérica é lot_area

consulta = "SELECT lot_area FROM PB_Tabela"
resultado = pd.read_sql_query(consulta, cnx)

lista_var_num = resultado['Lot_Area'].tolist()
print(lista_var_num)


print("\n14 - Consulta da tabela - agora contendo apenas os dados da variável categórica \n")
# Variável categórica é garage_type

consulta = "SELECT garage_type FROM PB_Tabela"
resultado = pd.read_sql_query(consulta, cnx)

lista_var_categoria = resultado['Garage_Type'].tolist()
print(lista_var_categoria)

###################################################################################
# 15 - crie uma estrutura de repetição que apresente na tela a soma dos valores acima da média dos valores da própria variável
###################################################################################

print("\n15 - Consumir Lista - crie uma estrutura de repetição para a soma dos valores acima da média dos valores da própria variável \n")
# Variável numérica é lista_var_num criada no item 13

media = mean(lista_var_num)
soma_val_media = 0

for valor in lista_var_num:
    if valor > media:
        soma_val_media += valor

print("A soma dos valores acima da média é: {:.2f}".format(soma_val_media))

###################################################################################
# 16 - crie uma função que, ao ser aplicada na lista (a lista deve ser passada para a função), retorne a contagem de ocorrência dos itens individuais da variável categórica
###################################################################################

print("\n16 - Consumir Lista - uma função que retorne a contagem de ocorrência dos itens individuais da variável categórica \n")
# Variável categórica é lista_var_categoria criada no item 14

def count_garage(lista):
    contagem = {}
    for categoria in lista:
        if categoria in contagem:
            contagem[categoria] += 1
        else:
            contagem[categoria] = 1
    return contagem

lista_var_categoria = resultado['Garage_Type'].tolist()

resultado = count_garage(lista_var_categoria)

for categoria, quantidade in resultado.items():
  if categoria == '':
    print(f"Casas com a Garagem 'NULL' constam {quantidade} vezes na lista.")
  else:
    print(f"Casas com a Garagem '{categoria}' constam {quantidade} vezes na lista.")


# Sempre executar um COMMIT e fechar a conexão antes de prosseguir
cnx.commit()
cnx.close()