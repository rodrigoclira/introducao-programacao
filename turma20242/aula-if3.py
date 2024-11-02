categoria = int(input("Informe a categoria: "))

if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    preco = 0

if preco != 0:
    print(f"O valor da categoria é {categoria:.2f}")
else:
    print("Categoria não encontrada")