def check_passwd(senhas):
    contador = 0

    for senha in senhas:
        rule, passwd_txt = senha.split(":")
        limite, caracter = rule.split()
        limite_min, limite_max = map(int, limite.split("-"))

        
        passwd_txt = passwd_txt.strip()

        caracter_count = passwd_txt.count(caracter)


        if limite_min <= caracter_count <= limite_max:
            contador += 1

    return contador



def read(filename):
    with open(filename, "r") as arquivo:
        senhas = []
        for linha in arquivo:
            senhas.append(linha.rstrip("\n"))
    return senhas



file1 = read("exemplo1.txt")
check_file1 = check_passwd(file1)
print(f'Teste 1 - Total de senhas válidas: {check_file1}')

file1 = read("exemplo2.txt")
check_file2 = check_passwd(file1)
print(f'Teste 2 - Total de senhas válidas: {check_file2}')
