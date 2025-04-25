km = float(input("Indique a quantidade de km da viagem: "))

if km <= 200:
    preco = 0.5
else:
    preco = 0.45

print(f"O preço da passagem para {km} km é R$ {preco * km:.2f}")
