from funcionalidades import insere_cadastro, altera_cpf, troca_sobrenomes, remove_cadastro, lista_cadastros, carregar_arquivos_json, salvar_arquivos_json


def menu():
  '''
  Apresenta o menu ao usuário.
  Retorna a opção selecionada (str).
  '''
  # Apresenta o menu
  print()
  print('Opções:')
  print('[1] Inserir novo cadastro')
  print('[2] Alterar CPF')
  print('[3] Trocar sobrenomes')
  print('[4] Remover cadastro')
  print('[5] Listar todos os cadastros')
  print('[6] Encerrar')
  
  # Retorna a opção do usuário
  print('\nDigite o nº da opção desejada:')
  return input()


# Armazenamento dos cadastros
cadastros = carregar_arquivos_json()

while True:
  opcao = menu()
  if opcao == '1':
    print(insere_cadastro(cadastros))
  elif opcao == '2':
    print(altera_cpf(cadastros))
  elif opcao == '3':
    print(troca_sobrenomes(cadastros))
  elif opcao == '4':
    print(remove_cadastro(cadastros))
  elif opcao == '5':
    lista_cadastros(cadastros)
  elif opcao == '6': # Encerrar
    salvar_arquivos_json(cadastros)
    print('Até logo!')
    break
  else:  # Opção inexistente
    print('Opção inválida') 