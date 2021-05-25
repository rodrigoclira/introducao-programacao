num = int(input("Informe o número: "))

primo = True
cont = 2
while cont < num:
    if num % cont == 0:
        print(cont)
        primo = False
        break
    cont +=1

print(f"O número {num} é primo: {primo}")