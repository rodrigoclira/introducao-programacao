
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
        continuar = input("Imprimir novamente (s/n): ")
        if continuar == "s":
            print("Você escolheu imprimir novamente...")
            continue
        cont+=1
    num+=1
    print()
