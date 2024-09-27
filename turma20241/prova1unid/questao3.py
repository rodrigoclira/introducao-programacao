
somaQuadrado = 0
soma = 0
cont = 1

while cont <= 100:
    somaQuadrado += cont ** 2
    soma += cont
    cont+=1

resultado = (soma ** 2) - somaQuadrado
print(f"O resultado é {resultado}")