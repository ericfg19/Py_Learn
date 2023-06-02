def peso_max(pesos_esmeraldas):
    num = len(pesos_esmeraldas)
    dp = [0] * (num + 1)  
  
    dp[0] = 0

    for i in range(1, num + 1):
        if pesos_esmeraldas[i - 1] % 2 == 0:
            dp[i] = max(dp[i - 1], dp[i - 2] + pesos_esmeraldas[i - 1])
        else:
            dp[i] = dp[i - 1]

    return dp[num]

# Entrada dos pesos das esmeraldas
pesos_esmeraldas = input("Digite os pesos das esmeraldas separados por espaço: ").split()
pesos_esmeraldas = [int(peso) for peso in pesos_esmeraldas]

peso_total_sum = peso_max(pesos_esmeraldas)
print("Maior peso total de esmeraldas que você pode comprar:", peso_total_sum)
