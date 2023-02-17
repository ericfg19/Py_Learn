conta = float(input("Informe o valor de consumo : R$ "))
percent = 20
servf = conta * percent/100
valorfinal = float(conta + servf)

print(f"O valor da taxa de gorjeta é 20%, portanto, será adicionado o valor de R$ {servf}")

print(f"O valor total da conta, com a taxa de gorjeta, será de R$ {valorfinal}.")
