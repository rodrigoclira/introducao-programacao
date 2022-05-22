
#num  = int(input("Numero: "))
num = 1
parar = False
while num <= 10:
    print(f"Calculando tabuada de multiplicação do {num}")
    cont = 0
    while cont <= 10:
        op = num*cont
        #print(f"{num} x {cont} = {num*cont}")
        print(f"{num} x {cont} = {op}")
        cont+=1
        continuar = input("Continuar (s/n): ")
        if continuar == "n":
            print("Você escolheu parar...")
            parar = True
            break
    num+=1
    if parar:
        break
    print()