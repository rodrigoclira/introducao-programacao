num = int(input("Informe o número: "))

divisores = 0
cont = 1
while cont <= num:
    if num % cont == 0:
        divisores += 1 
    cont +=1

if divisores == 2:
    print("É primo!")
else:
    print("Não é primo!")
