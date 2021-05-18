import random

m = int(input("Quantidade de linhas: "))
n = int(input("Quantidade de colunas: "))
matriz = []
contM = 0
#contN = 0

while contM < m: #linhas
    linha = []
    contN = 0
    while contN < n:
        valor = random.randint(1,9)
        linha.append(valor)
        contN +=1    
    matriz.append(linha)
    contM += 1
print(matriz)

contM=0
while contM < m:
    contN=0
    while contN < n:
        print(matriz[contM][contN], end=" ")
        contN+=1
    print("")
    contM+=1
