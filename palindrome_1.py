palavra = input("Informe uma palavra para verificar se a mesma é um palíndromo: ").strip().upper()


inverso = palavra[::-1]
print(f'Você digitou "{palavra}". Ao contrário, ela fica "{inverso}"')

if (inverso == palavra):
    print("Ela é um palíndromo!")
else:
    print("Infelizmente, ela não é um palíndromo!")