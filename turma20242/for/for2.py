notas = []

for i in range(3):
    nota = float(input(f"Informe a nota {i+1}: "))
    notas.append(nota)

print(sum(notas)/len(notas))