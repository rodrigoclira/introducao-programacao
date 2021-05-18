numero = input("Informe o número: ")

if int(numero) < 0:
    print("Número inválido")
else:
    soma = 0
    for digito in numero:
        soma += int(digito)

    print(f"A soma dos digitos de {numero} é {soma}")
