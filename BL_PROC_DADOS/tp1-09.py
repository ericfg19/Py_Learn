def formar_triangulo(a, b, c, d):
    if (a + b > c and a + c > b and a + d > b and b + c > a and b + d > a and c + d > a):
        return 'S'
    else:
        return 'N'

# Exemplo de uso da função
print(formar_triangulo(2, 3, 4, 5))  # deve imprimir "S"
print(formar_triangulo(2, 3, 6, 5))  # deve imprimir "N"