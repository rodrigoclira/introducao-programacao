preco_antigo = float(input("Informe o preço antigo do produto: "))

if preco_antigo <= 50:
    perc = 0.05
elif preco_antigo <= 100:
    perc = 0.1
else:
    perc = 0.15

novo_preco = preco_antigo + preco_antigo * perc
print(f"O novo preço do produto é R$ {novo_preco:.2f}")

