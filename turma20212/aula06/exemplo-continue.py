
cont = 0
while cont < 5:
    positivo = int(input(f"Informe um valor positivo ({cont+1}): "))
    
    if positivo < 0: 
        print("Esse valor é invalido")
        continue
    
    cont+=1