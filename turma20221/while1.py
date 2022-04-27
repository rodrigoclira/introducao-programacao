
quantidade = int(input("Quantidade de números: "))

cont = 1
num = 0
soma = 0
while cont <= quantidade:
    #print(cont)
    num = int(input(f"Informe o número ({cont}): "))
    soma+=num
    cont+=1
print(soma)
