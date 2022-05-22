quantidade_hab = int(input("Informe a quantidade de habitantes: "))

cont = 1
consumo_res = 0
consumo_ind = 0
consumo_com = 0
consumo_total = 0
maior = -1
menor = 2000

while cont <= quantidade_hab:
    consumo = float(input(f"Consumo ({cont}): "))
    codigo = int(input(f"Informe o códito (1,2,3) : "))
    
    if codigo == 1:
        consumo_res += consumo
    elif codigo == 2:
        consumo_com += consumo
    elif codigo == 3:
        consumo_ind += consumo
    else:
        print("Opção inválida")
        continue
    
    if cont == 1:
        maior = consumo
        menor = consumo
        
    if consumo > maior:
        maior = consumo
    
    if consumo < menor:
        menor = consumo
        
    consumo_total += consumo
    cont+=1

media = consumo_total / quantidade_hab
media = (consumo_res + consumo_ind + consumo_com) / quantidade_hab

print(f"Média:{media}\nMaior:{maior}\nMenor:{menor}")
print(f"TRes:{consumo_res}\nTCom:{consumo_com}\nTInd:{consumo_ind}")