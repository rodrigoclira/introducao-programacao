num = int(input("Número da tabuada: "))

cont=0
while cont <= 10:
    print(f"{num:02d} + {cont:02d} = {num+cont:02d}")
    cont+=1