conta = float(input("Informe o valor de consumo : R$ "))
pessoas1 = int(input("Informe o número de pessoas : "))
while pessoas1 < 1 :
    print("Número de pessoas inválido.")
    pessoas1 = int(input("Informe o número de pessoas (acima de 1): "))

percent1 = float(input("Informe o percentual do garçom : "))
while percent1 >= 100 :
    print("Percentual inválido.")
    percent1 = float(input("Informe o percentual do garçom (entre 0 a 100): "))
    
print('\n')

## Calculo
servf = conta * percent1/100
valorfinal = float(conta + servf)

div = float(valorfinal / pessoas1)

valorfinal = str(valorfinal).replace('.', ',')
div = str(div).replace('.', ',')


## Resultado

print(f"O valor total da conta, com a taxa de serviço, será de R$ {valorfinal}.")
print('\n')
print(f"Dividindo a conta por {pessoas1} pessoa(s), cada pessoa deverá pagar R$ {div}.")