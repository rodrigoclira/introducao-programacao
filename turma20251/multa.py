velocidade = int(input("Informe a velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"A multa a ser paga é R$ {multa:.2f}")
else:
    print("Não houve multa!")
