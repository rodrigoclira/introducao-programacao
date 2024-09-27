

def situacao_academica(notas, carga_horaria, frequencia):
    
    porc_presenca = frequencia/carga_horaria

    print(f"A presença foi {porc_presenca * 100}%")
    if (porc_presenca < 0.75): # se falou 50% entao reprovado
        return "REPROVADO POR FALTA"
    
    media = sum(notas) / len(notas) # sum
    print(f"A média foi {media}")

    if media >= 7:
        return "APROVADO POR MÉDIA"
    else:
        return "REPROVADO POR MÉDIA"


