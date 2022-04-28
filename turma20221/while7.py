inicio = int(input("Informe o início: ")) #1
fim = int(input("Informe o fim: ")) #10
cont = inicio
soma = 0
mult = 1
while cont <= fim:
    if cont % 2 == 0:
        #print(f"Par = {cont}")
        soma = soma + cont
    else:
        #print(f"Impar = {cont}")
        mult = mult * cont
    cont+=1

print(f"A soma dos números foi: {soma}")
print(f"A multiplicação dos números foi: {mult}")