A = {3, 4, 5, 6, 7, 8, 9, 10}
B = {9, 10, 11, 12}
C = {5, 7, 9, 11, 13}

#calcular barycentric
barycentric = A - (B.union(C))

print(f'{barycentric}')