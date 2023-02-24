# Imprimindo mensagem inicial e pegando nomes da entrada
print("Bem-vindo ao jogo da fusão!")
nome1 = input("Digite um nome completo (Nome Sobrenome): ")
nome2 = input("Digite outro nome completo (Nome Sobrenome): ")

# Separando nomes e sobrenomes
espaco = nome1.find(" ")
pn1 = nome1[:espaco]     # = nome1[0:espaco]
sn1 = nome1[espaco+1:]   # = nome1[espaco+1:len(nome1)]
espaco = nome2.find(" ")
pn2 = nome2[:espaco]     # = nome2[0:espaco]
sn2 = nome2[espaco+1:]   # = nome2[espaco+1:len(nome2)]

# # Imprimindo nomes e sobrenomes separados
# print(pn1)
# print(sn1)
# print(pn2)
# print(sn2)

# Encontrando os índices do meio de cada nome/sobrenome
meio_pn1 = len(pn1) // 2
meio_pn2 = len(pn2) // 2
meio_sn1 = len(sn1) // 2
meio_sn2 = len(sn2) // 2

# Dividindo os primeiros nomes em 2 partes
esq_pn1 = pn1[:meio_pn1]
dir_pn1 = pn1[meio_pn1:]
esq_pn2 = pn2[:meio_pn2]
dir_pn2 = pn2[meio_pn2:]

# Dividindo os sobrenomes em 2 partes
esq_sn1 = sn1[:meio_sn1]
dir_sn1 = sn1[meio_sn1:]
esq_sn2 = sn2[:meio_sn2]
dir_sn2 = sn2[meio_sn2:]

# Formando a 1ª combinação
# (partes esquerdas do 1º nome + partes direitas do 2º)
novo_pn1 = esq_pn1.capitalize() + \
           dir_pn2.lower()
novo_sn1 = esq_sn1.capitalize() + \
           dir_sn2.lower()

# Formando a 2ª combinação
# (partes esquerdas do 2º nome + partes direitas do 1º)
novo_pn2 = esq_pn2.capitalize() + \
           dir_pn1.lower()
novo_sn2 = esq_sn2.capitalize() + \
           dir_sn1.lower()

# Imprimindo os novos nomes formados
print("Aqui estão 2 possibilidades, escolha a que preferir!")
print(novo_pn1, novo_sn1)
print(novo_pn2, novo_sn2)
