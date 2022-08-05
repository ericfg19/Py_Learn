def diagnosticar_auxilio(renda_familiar, num_integrantes):
    sal_minimo = 1045
    max_renda_familiar = 3 * sal_minimo
    max_renda_porpessoa = 0.5 * sal_minimo
    
    renda_familiar = round(renda_familiar, 2)
    max_renda_familiar = round(max_renda_familiar, 2)
    max_renda_porpessoa = round(max_renda_porpessoa, 2)
    
    renda_porpessoa = renda_familiar / num_integrantes
    renda_porpessoa = round(renda_porpessoa, 2)
    
    if renda_familiar <= max_renda_familiar :
        comparar_renda = "inferior ou igual"
    else:
        comparar_renda = "superior"
    
    if renda_porpessoa <= max_renda_porpessoa:
        comparar_rpessoa = "inferior ou igual"
    else:
        comparar_rpessoa = "superior"
    
    if renda_familiar <= max_renda_familiar or renda_porpessoa <= max_renda_porpessoa:
        elegivel = "pode"
    else:
        elegivel = "não pode"
    
    diagnostico = f"A renda familiar total, de R$ {renda_familiar}, é {comparar_renda} a R$ {max_renda_familiar}.\n"
    diagnostico += f"A renda mensal por pessoa é de R$ {renda_porpessoa}, {comparar_rpessoa} a R$ {max_renda_porpessoa}.\n"
    diagnostico +=  f"O cidadão {elegivel} ser beneficiário do Auxílio Emergencial."
    print(diagnostico)
        
##########################################################

renda_familiar = float(input("Informe a renda familiar total mensal: R$ "))
num_integrantes = float(input("Informe o número de membros da família: "))


diagnosticar_auxilio(renda_familiar , num_integrantes)


