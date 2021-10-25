# Somar n números. Parar de pedir se for digitado -1

cont1 = 0
flag = False
while cont1 < 4:
    cont2 = 0
    while cont2 < 3:
        if cont1 == cont2:
            print("Executando break")
            break
        print(f"{cont1} - {cont2}")
        cont2+=1

    print("Incrementando contador externo (cont1)")        
    cont1+=1