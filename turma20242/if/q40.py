custo_fabrica = float(input("Indique o custo do carro da fábrica: "))

if custo_fabrica <= 12000:
    custo_distribuidor = custo_fabrica * 0.05
    custo_imposto = 0
elif custo_fabrica > 12000 and custo_fabrica <= 25000:
    custo_distribuidor = custo_fabrica * 0.1
    custo_imposto = custo_fabrica * 0.15
else:
    custo_distribuidor = custo_fabrica * 0.15
    custo_imposto = custo_fabrica * 0.2

custo_consumidor = custo_fabrica + custo_imposto + custo_distribuidor

print(f"O valor do consumidor é R$ {custo_consumidor:.2f}")
print(f"O valor do imposto é R$ {custo_imposto:.2f}")
print(f"O valor do distribuidor é R$ {custo_distribuidor:.2f}")
