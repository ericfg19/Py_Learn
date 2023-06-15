def abrir_arquivo(file):
  try:
    #abrir arquivo
    with open(file, 'r') as filename:
      text = filename.read()
      print(f'Texto do arquivo: \n{text}')
  #mensagem de erro
  except FileNotFoundError:
    print('Arquivo não encontrado')

file = input("Digite o nome do arquivo: ")

abrir_arquivo(file)