from datetime import datetime, timedelta

def dias_consumo_preciso(medicoes):
    n_medicoes = len(medicoes)
    dias_precisos = 0
    consumo_total = 0
    
    for i in range(n_medicoes - 1):
        data1, consumo1 = medicoes[i]
        data2, consumo2 = medicoes[i+1]
        
        # Converte as datas para o formato datetime
        data1 = datetime.strptime(data1, '%d/%m/%Y')
        data2 = datetime.strptime(data2, '%d/%m/%Y')
        
        # Calcula a diferença de dias entre as datas
        diff_dias = (data2 - data1).days
        
        if diff_dias == 1:
            # Se a diferença for de 1 dia, adiciona o consumo ao total
            consumo_total += consumo2 - consumo1
            dias_precisos += 1
        
    return dias_precisos, consumo_total
    
# Exemplo de uso da função
medicoes = [('01/01/2022', 10), ('02/01/2022', 15), ('03/01/2022', 23), ('05/01/2022', 30), ('06/01/2022', 35)]
dias, consumo = dias_consumo_preciso(medicoes)
print('Dias com consumo preciso:', dias)
print('Consumo total:', consumo)