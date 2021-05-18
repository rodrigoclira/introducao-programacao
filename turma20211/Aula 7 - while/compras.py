carteira = 100
prods = 0

while carteira > 0:
    valor_produto = int(input("Valor Produto: "))

    if carteira - valor_produto >= 0:
        carteira = carteira - valor_produto
        prods += 1 
    else:
        print(f"Você só tem {carteira} e não pode comprar um produto de {valor_produto}")

print (f"Você levou {prods} produtos")