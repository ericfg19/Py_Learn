def processo_eleitoral(idade):
  # Primeiro analisaremos quem tem obrigatoriedade de voto.
    if idade >= 18 and idade < 70:
      print(f"O eleitor é obrigado a votar.")
    elif idade >= 16 or idade >= 70:
        print(f"O eleitor tem direito, porém, não tem obrigação de votar.")
    else:
        print(f"O eleitor não tem direito a voto.")


idade = int(input("Informe a idade do cidadão: "))
while idade < 1 :
    print("Idade inválida.")
    idade = int(input("Informe a idade do cidadão (acima de 0): "))
processo_eleitoral(idade)
print("\n")

print("************")   