import random

numeros = [2, 3, 4, 10]
quantidade = 3
sorteados = []
random.shuffle(numeros) # embaralhando os números

while len(sorteados) < quantidade:
    sorteado = random.choice(numeros) # escolhendo um item aleatório
    if sorteado not in sorteados:
        sorteados.append(sorteado)
        print(f"O número {sorteado} foi sorteado")
    else:
        print(f"O número {sorteado} já foi sorteado anteriormente")
        print("Escolhendo outro...")
    
print(sorteados)    
    
    