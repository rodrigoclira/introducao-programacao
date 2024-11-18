soma = 0
cont = 0

while True:
    numero = int(input("Informe um numero inteiro para a soma ou digite 0 para sair: "))
    if numero == 0:
        break

    if numero < 0:
        continue
    
    soma += numero
    cont += 1

media = soma / cont
print(f"quantidade de numeros digitados: {cont}\nsoma dos numeros: {soma}\nMedia aritmetica dos numeros: {media}")