
print("Programa para calcular as médias dos alunos")

notas = []

while len(notas) < 5:
    print(f"Você digitou {len(notas)} notas. Informe mais uma...")
    nota_atual = float(input("Nota atual : "))
    notas.append(nota_atual)