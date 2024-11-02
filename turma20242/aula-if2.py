distancia = float(input("Indique a distância percorrida: "))

#if tipo_compra  "prazo":
    
if distancia <= 200:
    preco_km = 0.5
else:
    preco_km = 0.45

valor = preco_km * distancia
print(f"O custo da sua corrida será R$ {valor:.2f}")