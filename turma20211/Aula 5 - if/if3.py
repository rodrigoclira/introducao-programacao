media_semestre = float(input("Média semestral: "))
faltas = int(input("Faltas na disciplina: "))
aulas = int(input("Carga horária em aula: "))

if faltas/aulas > 0.25:
    print("Reprovado por falta")
elif media_semestre >= 7:
    print("Parabéns você foi aprovado")
elif media_semestre >= 3: #and media_semestre < 7:
    print("Você pode fazer a final")
    nota_final = float(input("nota final: "))
    media = (nota_final +  media_semestre)/2
    if media >= 5:
        print("Parabéns você foi aprovado na final")
    else:
        print("Reprovado na final")
else:
    print("Reprovado por nota")
