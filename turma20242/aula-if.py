velocidade = int(input("Informe a velocidade: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"A sua multa foi R$ {multa:.2f}")