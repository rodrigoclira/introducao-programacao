lista = []
cont=1
while cont <= 8:
    valor = int(input(f"Valor {cont}: "))
    lista.append(valor)
    cont+=1

maior = lista[0] 
cont=1
while cont<len(lista):
    if lista[cont] > maior:
        maior = lista[cont]
    cont+=1
 (maior)
