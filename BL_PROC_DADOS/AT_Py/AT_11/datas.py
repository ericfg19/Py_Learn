from datetime import date


# Lista com nº de dias de cada mês
DIAS_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def data_futura(data):
  '''
  data: Data a ser verificada (str)
  Verifica se a data é futura.
  Retorna True se a data for futura, False caso contrário.
  '''
  hoje = date.today()
  # Separa e converte os campos da data
  dia = int(data[:2])
  mes = int(data[3:5])
  ano = int(data[6:])
  
  if ano < hoje.year:
    return False
    
  if ano == hoje.year:  # Se é este ano
    if mes < hoje.month:
      return False
      
    if mes == hoje.month:  # Se é este mês
      return dia > hoje.day

  return True


def ano_bissexto(ano):
  '''
  ano: Ano a ser verificado (int)
  Verifica se o ano é bissexto.
  Retorna True se o ano for bissexto, False caso contrário.
  '''
  return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)


def idade_dias(data_nasc):
  '''
  data_nasc: Data de nascimento (str)
  Calcula o nº de dias decorridos desde o nascimento.
  Retorna a idade em dias (int).
  '''
  hoje = date.today()
  # Separa e converte os campos da data de nascimento
  dia_nasc = int(data_nasc[:2])
  mes_nasc = int(data_nasc[3:5])
  ano_nasc = int(data_nasc[6:])

  # Calcula a idade da pessoa em dias
  # Inicializa a contagem de dias em zero
  dias = 0

  # Para cada ano desde o nascimento da pessoa...
  for ano in range(ano_nasc, hoje.year + 1):
    # Define o 1º mês a ser contado no ano
    mes_inicial = 1

    # Se for ano de nascimento, começa a contar do mês de nascimento
    if ano == ano_nasc:
      mes_inicial = mes_nasc
      
    # Define o último mês a ser contado no ano
    mes_final = 12
    
    # Se for ano em que estamos, conta até o mês em que estamos
    if ano == hoje.year:
      mes_final = hoje.month
      
    # Para cada mês a ser contado neste ano...
    for mes in range(mes_inicial, mes_final + 1):
      # Se forem o ano e o mês em que estamos, soma o dia de hoje
      if ano == hoje.year and mes == hoje.month:
        dias += hoje.day
      else:
        # Senão, soma o nº de dias do mês
        dias += DIAS_MES[mes - 1]

        # Se for fevereiro e o ano for bissexto, soma mais 1 dia
        if mes == 2 and ano_bissexto(ano):
          dias += 1
      
      # Se forem o ano e o mês de nascimento, 
      # subtrai o dia de nascimento
      if ano == ano_nasc and mes == mes_nasc:
        dias -= dia_nasc
        
  return dias
