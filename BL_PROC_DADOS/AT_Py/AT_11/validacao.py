from datas import ano_bissexto, DIAS_MES


def id_valido(total, uid, ins=False):
  '''
  total: Nº de cadastros existentes (int)
  uid: ID a ser validado (str)
  ins: Validação para inserção (bool, padrão: False)
  Verifica se o valor de `uid` representa um ID válido.
  Retorna True se o ID for válido, False caso contrário.
  '''
  if ins:
    limite = total + 2
  else:
    limite = total + 1
    
  return uid.isdecimal() and (0 < int(uid) < limite)


def nome_valido(nome):
  '''
  nome: Nome a ser validado (str)
  Verifica se o valor de `nome` representa um nome válido.
  Retorna True se o nome for válido, False caso contrário.
  '''
  return nome.isalpha()


def cpf_valido(cpf):
  '''
  cpf: CPF a ser validado (str)
  Verifica se o valor de `cpf` representa um CPF válido.
  Retorna True se o CPF for válido, False caso contrário.
  '''
  # Valida o CPF
  if cpf.isdecimal() and len(cpf) == 11:
    # Valida 1º dígito verificador
    soma = 0
    for i in range(9):
      soma += int(cpf[i]) * (10 - i)
    r = soma % 11
    if r < 2:
      dv = 0
    else:
      dv = 11 - r
    if int(cpf[9]) == dv:
      # Valida 2º dígito verificador
      soma = 0
      for i in range(1, 10):
        soma += int(cpf[i]) * (11 - i)
      r = soma % 11
      if r < 2:
        dv = 0
      else:
        dv = 11 - r
      return int(cpf[10]) == dv
      
  return False


def cpf_sudeste(cpf):
  '''
  cpf: CPF a ser verificado (str)
  Verifica se o CPF é da Região Sudeste.
  Retorna True se for do Sudeste, False caso contrário.
  '''
  return 5 < int(cpf[8]) < 9


def data_valida(data):
  '''
  data: Data a ser validada (str)
  Verifica se o valor de `data` representa uma data válida.
  Retorna True se a data for válida, False caso contrário.
  '''
  # Valida a data
  if (len(data) == 10 and 
      data[:2].isdecimal() and 
      data[3:5].isdecimal() and 
      data[6:].isdecimal() and 
      data[2] == data[5] == '/'):
    # Separa e converte os campos da data
    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    if 0 < ano:
      if 0 < mes < 13:
        if mes == 2 and ano_bissexto(ano):
          return 0 < dia < 30
        else:
          return 0 < dia <= DIAS_MES[mes - 1]

  return False
