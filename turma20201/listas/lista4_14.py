import random
cartela = []
repo = list(range(100))
i = 0

while i < 5:
    j=0
    linha = []
    while j < 5:
        random.shuffle(repo)
        pos = random.randint(0, len(repo)-1)
        valor_sorteado = repo.pop(pos)
        linha.append(valor_sorteado)
        j+=1
    cartela.append(linha)
    i+=1

print(cartela)
