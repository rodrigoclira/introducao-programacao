dinheiro = 100
compra = 0

while dinheiro > 0:
    gasto = int(input('Quanto você gastou: '))
    if gasto > dinheiro:
        print('Você não tem dinheiro suficiente!')
    else:
        dinheiro = dinheiro - gasto
        compra += 1        
    print(f"Você possui {dinheiro:.2f}")

print(f"Você comprou {compra} produtos\nSeu saldo atual é: {dinheiro:.2f}")