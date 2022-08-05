import matplotlib.pyplot as plt

def calc_deprec(modelo, valor, vida_util):
    
    depre_anual = valor / vida_util
    depre_mensal = depre_anual / 12
    
    valores_mensais = []
    valor = valor * 0.90
    print(f"Depreciação do {modelo} ao longo de 12 meses:")
    print(f"• A sair da concessionária, o veículo perde 10% do valor e vale {valor:.2f}.")
    
    for i in range(12):
        valor = valor - depre_mensal
        valores_mensais.append(valor)
        print(f"\t• Após {i+1} mês(es) de uso, o carro vale: R$ {valor:.2f}. ")


    plt.plot(valores_mensais)
    plt.show()


#######################
modelo = input("Informe o nome do modelo: ")
valor = float(input("Informe o valor do carro 0 KM: R$ "))
vida_util = int(input("Informe a vida útil do carro, em anos: "))


calc_deprec(modelo, valor, vida_util)