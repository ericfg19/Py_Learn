def calc(calculo):
  operator = calculo[0]
  num1 = int(calculo[1::2])
  num2 = int(calculo[2::2][::-1])

  if operator == '+':  
    result = num1 + num2
  elif operator == '-': 
      result = num1 - num2
  elif operator == '*':
      result = num1 * num2
  elif operator == '/':
      result = num1 / num2
  else:
      print("Erro: Operador Invalido!\n")  
      return None
  
  return result

print("Menu de Operadores \nSOMA (+)\nSUBTRAÇÃO = -\nMULTIPLICAÇÃO = *\nDIVISÃO = /\n")
calculo = input("Digite o operador: ")

result = calc(calculo)
print(f'Resultado: {result:.3f}')
