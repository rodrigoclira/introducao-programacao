lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
cont = 0

while cont < 5:
    valor = int(input(f"Valor ({cont}) da lista1: "))
    lista1.append(valor)

    valor = int(input(f"Valor ({cont}) da lista2: "))
    lista2.append(valor)

    lista3.append(lista1[cont] + lista2[cont])
    lista4.append(lista1[cont] - lista2[cont])
    lista5.append(lista1[cont] * lista2[cont])
    cont+=1

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)