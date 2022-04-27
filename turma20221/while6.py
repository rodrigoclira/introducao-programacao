#num = int(input("Número da tabuada: "))
num = 1
while num <= 10:
    cont=0
    print(f"Tabuada de {num}")
    while cont <= 10:
        print(f"{num:02d} + {cont:02d} = {num+cont:02d}")
        cont+=1
    num+=1
