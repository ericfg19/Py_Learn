import matplotlib
import matplotlib.pyplot as plt
import time
##input
renda = float(input("Informe um valor inicial de renda: "))
juros_tempo = float(input("Rendimento por período (%): "))
aporte = float(input("Aporte a cada período: "))
periodo = int(input("Total de períodos: "))
##Calculo & arrays

juros_tempo = juros_tempo / 100
tempo = 1

periodografico = []
rendagrafico = []

##Saída Tempo
time.sleep(0.5) 
print("\n")
while tempo <= periodo :
    renda = renda * (juros_tempo + 1) + aporte
    print(f"Após {tempo} periodos, o montante será de {renda:.2f}.")
    tempo = tempo + 1
    rendagrafico.append(renda)
    periodografico.append(tempo)
time.sleep(0.5)
print("\n")
print("******************")
##

matplotlib.pyplot.plot(periodografico, rendagrafico)
matplotlib.pyplot.show()