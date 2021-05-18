qtd_notas = int(input("Quantidade de notas: "))
cont = 1
soma_total = 0

while cont <= qtd_notas:
    valor_nota = float(input(f"Valor da nota {cont}: "))
    soma_total += valor_nota
    cont+=1

print(f"Média das {qtd_notas} foi {soma_total/qtd_notas : .2f}")