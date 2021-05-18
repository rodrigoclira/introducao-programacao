numero = input("Digite um número: ")

if int(numero) < 0:
    print("número inválido")
else:
    contador = 0
    soma = 0
    while contador < len(numero):
        soma += int(numero[contador])
        contador += 1
    print(soma)
