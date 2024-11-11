cont = 1
soma = 0

while cont <= 5:
    numero = float(input(f"Informe o número ({cont}):"))
    soma += numero
    cont+=1

media = soma / 5
print (f"A média dos 5 números é {media:.2f}")