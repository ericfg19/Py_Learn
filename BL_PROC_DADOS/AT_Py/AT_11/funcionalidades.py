from datas import data_futura, idade_dias
from validacao import id_valido, nome_valido, cpf_valido, cpf_sudeste, data_valida


import os
import json

def insere_cadastro(cadastros):
  '''
  cadastros: Estrutura que armazena os cadastros (list)
  Insere um novo cadastro com dados fornecidos pelo usuário.
  Retorna uma mensagem com o resultado da operação (str).
  '''
  # Lê o ID
  uid = input('ID (opcional): ')
  if (uid != '' and 
      not id_valido(len(cadastros), uid, True)):
    return 'ID inválido'
    
  # Lê o primeiro nome
  nome = input('Primeiro nome: ').capitalize()
  if not nome_valido(nome):
    return 'Nome inválido'
    
  # Lê o sobrenome
  sobrenome = input('Sobrenome: ').capitalize()
  if not nome_valido(sobrenome):
    return 'Sobrenome inválido'
    
  # Adiciona o sobrenome ao nome
  nome += ' ' + sobrenome
  
  # Lê o CPF
  cpf = input('CPF (apenas dígitos): ')
  if not cpf_valido(cpf):
    return 'CPF inválido'
  if cpf_sudeste(cpf):
    return 'CPF não aceito por ser do Sudeste'
    
  # Lê a data de nascimento
  data_nasc = input('Data de nascimento (dd/mm/aaaa): ')
  if not data_valida(data_nasc):
    return 'Data de nascimento inválida'
  if data_futura(data_nasc):
    return 'Data de nascimento não pode ser futura'

  novo_cadastro = {'nome': nome,
                   'cpf': cpf,
                   'nasc': data_nasc}

  if uid == '':  # ID não preenchido
    # Insere cadastro no final
    cadastros.append(novo_cadastro)
  else:  # ID preenchido
    # Insere cadastro na posição correspondente ao ID
    cadastros.insert(int(uid) - 1, novo_cadastro)

  return 'Cadastro inserido com sucesso'


def altera_cpf(cadastros):
  '''
  cadastros: Estrutura que armazena os cadastros (list)
  Altera o CPF de um cadastro indicado pelo usuário.
  Retorna uma mensagem com o resultado da operação (str).
  '''
  # Lê o ID
  uid = input('ID: ')
  if not id_valido(len(cadastros), uid):
    return 'ID inválido'
  
  # Lê o CPF
  cpf = input('CPF (apenas dígitos): ')
  if not cpf_valido(cpf):
    return 'CPF inválido'
  if cpf_sudeste(cpf):
    return 'CPF não aceito por ser do Sudeste'

  # Atualiza o CPF
  cadastros[int(uid) - 1]['cpf'] = cpf

  return 'CPF atualizado com sucesso'


def troca_sobrenomes(cadastros):
  '''
  cadastros: Estrutura que armazena os cadastros (list)
  Troca os sobrenomes de 2 cadastros indicados pelo usuário.
  Retorna uma mensagem com o resultado da operação (str).
  '''
  # Lê o 1º ID
  uid = input('1º ID: ')
  if not id_valido(len(cadastros), uid):
    return 'ID inválido'
  uid1 = int(uid)
  
  # Lê o 2º ID
  uid = input('2º ID: ')
  if not id_valido(len(cadastros), uid):
    return 'ID inválido'
  uid2 = int(uid)

  # Divide os nomes correspondentes em primeiro nome e sobrenome
  nome1 = cadastros[uid1 - 1]['nome'].split()
  nome2 = cadastros[uid2 - 1]['nome'].split()
  
  # Troca os sobrenomes, atualizando os cadastros
  cadastros[uid1 - 1]['nome'] = nome1[0] + ' ' + nome2[1]
  cadastros[uid2 - 1]['nome'] = nome2[0] + ' ' + nome1[1]

  return 'Sobrenomes trocados com sucesso'


def remove_cadastro(cadastros):
  '''
  cadastros: Estrutura que armazena os cadastros (list)
  Remove um cadastro indicado pelo usuário.
  Retorna uma mensagem com o resultado da operação (str).
  '''
  # Lê o ID
  uid = input('ID: ')
  if not id_valido(len(cadastros), uid):
    return 'ID inválido'

  #  Remove os valores do cadastro correspondente
  cadastros.pop(int(uid) - 1)

  return 'Cadastro removido com sucesso'


def lista_cadastros(cadastros):
  '''
  cadastros: Estrutura que armazena os cadastros (list)
  Apresenta os dados de todos os cadastros.
  '''
  # Se não há nenhum cadastro, imprime mensagem informando
  if len(cadastros) == 0:
    print('Nenhum cadastro')
    return

  # Para cada cadastro...
  for uid, cadastro in enumerate(cadastros, 1):
    # Imprime os dados do cadastro
    print()
    print('ID:', uid)
    print('Nome:', cadastro['nome'])
    print('CPF:', cadastro['cpf'])
    print('Data de nascimento:', cadastro['nasc'])
    print('Idade em dias:', idade_dias(cadastro['nasc']))


#### TESTE ADIÇÃO E ALTERAÇÕES PARA ARQUIVO DE CADASTROS


current_cwd = os.getcwd()
records_file = os.path.join(current_cwd, "cadastros.json")

json_fields = ["nome", "cpf", "nasc"]

def carregar_arquivos_json():
    try:
        if not os.path.exists(records_file):
            return []
        
        with open(records_file, "r") as f:
            data = json.load(f)

        return data
    except Exception as ex:
        print(f"Erro ao ler arquivo: {ex}")
        return []

def salvar_arquivos_json(cadastros):
    try:
        with open(records_file, "w") as f:
            json.dump(cadastros, f, indent=4)
    except Exception as ex:
        print(f"Erro ao cadastrar arquivo: {ex}")
