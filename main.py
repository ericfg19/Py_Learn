from selenium import webdriver

from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome('C:/chromedriver_win32/chromedriver')


# Substitui só para testar se abre o site do BB
# browser.get('https://google.com')
browser.get('https://www63.bb.com.br/portalbb/djo/id/IdDeposito,802,4647,4648,0,1.bbx?pk_vid=a8c030459b6e546b1624899559a5e218&pk_vid=a8c030459b6e546b1624899559a5e218&pk_vid=a8c030459b6e546b1624900138a5e218&#8203;&pk_vid=c232b04747645307166878141098691e&pk_vid=c232b04747645307166878141098691e&pk_vid=c232b04747645307166878141098691e')

time.sleep(2)


################################### SÓ EXECUTA NO INÍCIO ################################
#TIPO DE JUSTIÇA
search_input_radio_button = browser.find_element(By.XPATH, '//*[@id="formularioIdDeposito:justica:0"]')
search_input_radio_button.click()

time.sleep(0.5)

#PRÉ CADASTRAMENTO
search_input_escolha = browser.find_element(By.XPATH, '//*[@id="formularioIdDeposito:optTipoCadastramento"]')
search_input_escolha.send_keys('Primeiro depósito')

time.sleep(0.5)

#CONTINUAR
search_input_continuar = browser.find_element(By.XPATH, '//*[@id="formularioIdDeposito:btnContinuar"]')
search_input_continuar.click()

#########################################################################################



###################### REPETE ENQUANTO HOUVER REGITRO P/ PROCESSAR ######################

time.sleep(0.5)

#UNIDADE DA FEDERAÇÃO
search_input_UF = browser.find_element(By.XPATH, '//*[@id="formulario:comboUf"]')
search_input_UF.send_keys('RJ - RIO DE JANEIRO')

time.sleep(0.5)

#TRIBUNAL
search_input_tribunal = browser.find_element(By.XPATH, '//*[@id="formulario:cmbTribunal"]')
search_input_tribunal.send_keys('TRIBUNAL DE JUSTICA')

time.sleep(0.5)

#COMARCA
search_input_comarca = browser.find_element(By.XPATH, '//*[@id="formulario:cmbComarca"]')
search_input_comarca.send_keys('RIO DE JANEIRO')

time.sleep(0.5)

#CONTINUAR
search_input_continuar = browser.find_element(By.XPATH, '//*[@id="formulario:botaoContinuar"]')
search_input_continuar.click()

time.sleep(0.5)

#ÓRGÃO DE JUSTIÇA
search_input_orgao_de_justica = browser.find_element(By.XPATH, '//*[@id="formulario:cmbOrgaos"]')
search_input_orgao_de_justica.send_keys('AUDITORIA JUSTICA MILITAR')

time.sleep(0.5)

#NATUREZA DA AÇÃO
search_input_natureza_da_acao = browser.find_element(By.XPATH, '//*[@id="formulario:cmbAcoes"]')
search_input_natureza_da_acao.send_keys('PRECATORIO')

time.sleep(0.5)

#NÚMERO DO PROCESSO JUDICIAL
search_input_orgao_de_justica = browser.find_element(By.XPATH, '//*[@id="formulario:numeroProcesso"]')
search_input_orgao_de_justica.send_keys(1)

time.sleep(0.5)

#NÚMERO DA GUIA
search_input_natureza_da_acao = browser.find_element(By.XPATH, '//*[@id="formulario:numeroGuia"]')
search_input_natureza_da_acao.send_keys(2)

time.sleep(0.5)

#VALOR DO DEPÓSITO JUDICIAL
search_input_valor_do_deposito_judicial = browser.find_element(By.XPATH, '//*[@id="formulario:valorDeposito"]')
search_input_valor_do_deposito_judicial.send_keys(0.01)

time.sleep(0.5)
#DEPOSITANTE
search_input_depositante = browser.find_element(By.XPATH, '//*[@id="formulario:cmbTipoDepositante"]')
search_input_depositante.send_keys('Autor')

time.sleep(0.5)

#NOME AUTOR
search_input_nome_autor = browser.find_element(By.XPATH, '//*[@id="formulario:nomeAutor"]')
search_input_nome_autor.send_keys('Rubens Lopes de Oliveira')

time.sleep(0.5)

#TIPO DE PESSOA AUTOR
search_input_tipo_de_pessoa_autor = browser.find_element(By.XPATH, '//*[@id="formulario:cmbTipoPessoa"]')
search_input_tipo_de_pessoa_autor.send_keys('Física')

time.sleep(0.5)

#CPF AUTOR
search_input_cpf_autor = browser.find_element(By.XPATH, '//*[@id="formulario:cpfAutor"]')
search_input_cpf_autor.send_keys('59866900797')

time.sleep(0.5)

#ADVOGADO AUTOR
search_input_advogado_autor = browser.find_element(By.XPATH, '//*[@id="formulario:txtAdvAutor"]')
search_input_advogado_autor.send_keys('Frederick')

time.sleep(0.5)

#NOME RÉU
search_input_nome_autor = browser.find_element(By.XPATH, '//*[@id="formulario:nomeReu"]')
search_input_nome_autor.send_keys('Eriv Von Zipper')

time.sleep(0.5)

#TIPO DE PESSOA RÉU
search_input_tipo_de_pessoa_autor = browser.find_element(By.XPATH, '//*[@id="formulario:cmbTipoPessoaReu"]')
search_input_tipo_de_pessoa_autor.send_keys('Física')

time.sleep(0.5)

########################### PROBLEMA -> CORRIGIR ######################
#CPF RÉU
search_input_cpf_reu = browser.find_element(By.XPATH, '//*[@id="formulario:cpfReu"]')
search_input_cpf_reu.send_keys('08831020722')

time.sleep(0.5)

#ADVOGADO RÉU
search_input_advogado_autor = browser.find_element(By.XPATH, '//*[@id="formulario:txtAdvReu"]')
search_input_advogado_autor.send_keys('Michel Assef Filho')

time.sleep(0.5)

#OBSERVAÇÃO
search_input_observacao = browser.find_element(By.XPATH, '//*[@id="formulario:txtObs"]')
search_input_observacao.send_keys('NO OBSERVATIONS')

time.sleep(0.5)

#GERAR ID
search_input_gerar_id = browser.find_element(By.XPATH, '//*[@id="formulario:btnGerarID"]')
search_input_gerar_id.click()

time.sleep(3)

#RETORNAR
search_input_retornar = browser.find_element(By.XPATH, '//*[@id="formulario:btnRetornar"]')
search_input_retornar.click()

time.sleep(20)


