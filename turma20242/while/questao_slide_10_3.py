numero = int(input("informe o número da tabuada: "))

cont = 1
while cont <= 10:
    print(f"{numero:02d} + {cont:2d} = {numero + cont:02d}")
    cont = cont + 1