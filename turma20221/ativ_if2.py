# <= 200 R$ .5 / km
# > 200 R$  .45 / km

distancia = float(input("Informe a distância percorrida: "))

if distancia <= 200:
    print("entrou no if!")
    valor_pago = distancia * 0.5
elif distancia <= 400:
    print("entrou no elif!")
    valor_pago = distancia * 0.45
else:
    print("entrou no else!")
    valor_pago = distancia * 0.35
    
print(f"Para a distância de {distancia} km você vai pagar R$ {valor_pago}")
