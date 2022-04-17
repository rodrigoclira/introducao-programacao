# > 80  a multa será R$ 5 por km excedido

velocidade = int(input("Informe a velocidade: "))


if velocidade > 80:
    excedeu = (velocidade - 80) 
    multa = excedeu * 5
    print(f"A multa tem o valor de R$ {multa} porque\
você excedeu {excedeu} km")
else:
    print("Você não será multado!")

