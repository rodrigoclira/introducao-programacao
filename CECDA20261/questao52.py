saque = int(input("Digite o valor do saque: "))

notas = [100, 50, 20, 10, 5, 2, 1]
cont = 0

print("Notas necessárias:")
while cont < len(notas):
    quantidade = saque // notas[cont]
    if quantidade > 0:
        print(f"  {quantidade} nota(s) de R$ {notas[cont]}")
    saque = saque % notas[cont]
    cont += 1
