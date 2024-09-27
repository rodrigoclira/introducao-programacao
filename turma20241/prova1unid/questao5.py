
custo_fabrica = float(input("Custo da Fábrica: "))


if custo_fabrica <= 12000:
    custo_consumidor = custo_fabrica + (0.05 * custo_fabrica)
elif custo_fabrica <= 25000:
    custo_consumidor = custo_fabrica + (0.1 * custo_fabrica) + (0.15 * custo_fabrica)
elif custo_fabrica > 25000:
    custo_consumidor = custo_fabrica + (0.15 * custo_fabrica) + (0.2 * custo_fabrica)


print(f"Com o custo  de R$ {custo_fabrica:.2f}, o preço para o consumidor é R$ {custo_consumidor:.2f}")