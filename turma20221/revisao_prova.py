import random
#random.randint <- Inteiro aleatório
#random.shuffle <- Embaralhar uma lista
#random.choice  <- Escolher a posição lista de forma aleatoria

### ADONAI
        #0   1  2   3
lista = [1, 10, 20, 30]
escolhido = random.choice(lista)
index_escolhido = random.randint(0, len(lista) - 1) # 0, 3 

print(f"valor com choice {escolhido}")
print(f"Posição com indice (randint) {index_escolhido}")

matrix = [ [1,2] , [3,4] , [5,8] ]
escolhido = random.choice(matrix)
print(random.choice(escolhido))

random.shuffle(matrix)
print(matrix)

### José Augusto
matrix = [[1,2,3], [4,5,6], [7,8,9]]

#solução 1
vetor1 = []
for lista_interna in matrix:
    for item in lista_interna:
        vetor1.append(item)
print(vetor1)

#solução 2
vetor2 = []
for lista_interna in matrix:
    vetor2.extend(lista_interna)
print(vetor2)

# Criar dicionário partir do dicionário
dici = {}
for item in vetor1:
    dici[item] = 0

print(dici)

# Arthur
dici = {}
for i in range(0,11):
    dici[i] = 0
    
print(dici)

lista = [1, 10, 20, 30]
caracter_inicial = ord('A')
ALFABETO="ABCDEF"
for pos, item in enumerate(lista):
    caracter_atual = caracter_inicial + pos
    print(chr(caracter_atual), item)
    print(ALFABETO[pos], item)

# Kácio
# i x j

lim_lin = lim_col = 4
matriz = []
for lin in range(0, lim_lin):
    lista_interna = []
    for col in range(0, lim_col):
        sorteado = random.randint(0, 20)
        lista_interna.append(sorteado)
        print (f'{sorteado:2d}', end=' ') 
    matriz.append(lista_interna)
    print()

print(matriz)     
            