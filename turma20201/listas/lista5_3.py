import random

lista = []
for i in range(10):
    nome = input(f"Nome {i+1} :")
    lista.append(nome)

print(lista)
print("Embaralhando Lista")
random.shuffle(lista)
print(lista) #embaralhado
pos_sorteada = random.randint(0, len(lista)-1("Sorteado: ")
sorteado = lista.pop(pos_sorteada)
print(sorteado)

print("Lista Atual")
print(lista)
print("Embaralhando Lista")
random.shuffle(lista)
print(lista)
pos_sorteada = random.randint(0, len(lista)-1)
print("Novo Sorteado: ")
sorteado = lista.pop(pos_sorteada)
print(sorteado)
