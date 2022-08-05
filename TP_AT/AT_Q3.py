import time

ren_mensal = float(input("Renda mensal total: "))
gasto_moradia = float(input("Gastos totais com moradia: "))
gasto_edu = float(input("Gastos totais com educação: "))
gasto_transp = float(input("Gastos totais com transporte: "))

percent1 = ren_mensal * 0.30
percent2 = ren_mensal * 0.20
percent3 = ren_mensal * 0.15

percentual_moradia = gasto_moradia / ren_mensal * 100
percentual_edu = gasto_edu / ren_mensal * 100
percentual_transp = gasto_transp / ren_mensal * 100

print('\n')
time.sleep(0.4)
print("************")
if percent1 >= gasto_moradia :
    print(f"Seus gastos totais com moradia comprometem {percentual_moradia:.2f}% de sua renda total. O máximo recomendado é de 30%.\n Seus gastos com moradia estão dentro da margem recomendada.")
else:
    print(f"Seus gastos totais com moradia comprometem {percentual_moradia:.2f}% de sua renda total. O máximo recomendado é de 30%.\n Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {percent1:.2f}.")
time.sleep(0.5)
if percent2 >= gasto_edu :
    print(f"Seus gastos totais com educação comprometem {percentual_edu:.2f}% de sua renda total. O máximo recomendado é de 20%.\n Seus gastos com educação estão dentro da margem recomendada.")
else:
    print(f"Seus gastos totais com educação comprometem {percentual_edu:.2f}% de sua renda total. O máximo recomendado é de 20%.\n Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {percent2:.2f}.")
time.sleep(0.5)    
if percent3 >= gasto_transp :
    print(f"Seus gastos totais com transporte comprometem {percentual_transp:.2f}% de sua renda total. O máximo recomendado é de 15%.\n Seus gastos com transporte estão dentro da margem recomendada.")
else:
    print(f"Seus gastos totais com transporte comprometem {percentual_transp:.2f}% de sua renda total. O máximo recomendado é de 15%.\n Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {percent3:.2f}.")
time.sleep(0.7) 
print("************")
time.sleep(10)