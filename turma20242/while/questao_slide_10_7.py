

soma = 0 

while True:
    numero = int(input("Informe um valor para somar ou 0 para sair: "))
    if numero == 0:
        break
    soma += numero

print(soma)