

def calcular_consumo_ideal(tipo_carro):
    if tipo_carro == 'caminhonete':
        consumo_ideal = 8, 14
    else:
        consumo_ideal = 10, 15
    
    return consumo_ideal

def calcular_situacao_carro(distancia, litros, tipo_carro):
    consumo = distancia/litros
    primeiro, segundo = calcular_consumo_ideal(tipo_carro)
    if consumo <= primeiro:
        return "Venda o carro!"
    elif consumo <= segundo:
        return "Econômico!"
    else:
        return "Super Econômico"    

print("Cálculo de consumo")
distancia_percorrido = float(input("Informe a distância percorrida: ")) 
litros_usados = float(input("Informe a quantidade litros usados: "))
tipo_carro = input("Informe o tipo do carro: ")
res = calcular_situacao_carro(distancia_percorrido, litros_usados, tipo_carro)
print(res)