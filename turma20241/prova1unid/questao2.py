votoMaria = 0
votoJoao = 0
votoJoaquim = 0
votoJosefa = 0
nulos = 0
brancos = 0

voto = 1

while voto != 0:
    print("""1 - João
2 - João
3 - Joaquim
4 - Josefa
5 - Nulo
6 - Branco""")
    
    voto = int(input("Indique seu voto: "))

    if voto == 1:
        votoMaria = votoMaria + 1
    elif voto == 2:
        votoJoao += 1
    elif voto == 3:
        votoJoaquim += 1
    elif voto == 4:
        votoJosefa += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos +=1
    else: 
        print("Voto inválido")

print("\nResultados...")
print(f"Maria: {votoMaria}")
print(f"João: {votoJoao}")
print(f"Joaquim: {votoJoaquim}")
print(f"Josefa: {votoJosefa}")
print(f"Nulos: {nulos}")
print(f"Brancos: {brancos}")
total_votos = votoMaria + votoJoao + votoJoaquim + votoJosefa + nulos + brancos

#calculando a percentagem
perc_nulos = (nulos/total_votos) * 100
perc_brancos = (brancos/total_votos) * 100

print(f"Percentagem de nulos {perc_nulos}")
print(f"Percentagem de brancos {perc_brancos}")
