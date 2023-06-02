def contar_letras(texto):
    contador = {}
    
    # Contar repetição de cada letra
    for letra in texto:
        if letra.islower(): 
            contador[letra] = contador.get(letra, 0) + 1
    
    
    maior_contagem = max(contador.values())
    
    
    letras_mais_ocorrencias = [letra for letra, ocorrencias in contador.items() if ocorrencias == maior_contagem]
    
    return letras_mais_ocorrencias, maior_contagem


texto = input("Digite um texto: ")


letras_mais_ocorrencias, maior_contagem = contar_letras(texto)


print("Letras mais repetidas:", ", ".join(letras_mais_ocorrencias))
print("Número de repetições:", maior_contagem)
