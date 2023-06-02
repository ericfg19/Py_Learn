def mudar_negativo(lista):
    for i in range(len(lista)):
        if lista[i] <= 0:
            lista[i] = 1
    return lista

nums = input("Digite a lista de inteiros separados por espaço: ")
val_nums = list(map(int, nums.split()))


lista_result = mudar_negativo(val_nums)

print("Lista resultante:", lista_result)
