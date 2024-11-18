while True:

    print("""
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair\n""")
    
    opcao = int(input("Opção: "))

    if opcao == 5:
        break

    if opcao >= 1 and opcao <=5:
 
        op1 = float(input("Operador 1: "))
        op2 = float(input("Operador 2: "))

        if opcao == 1:
            resultado = op1 + op2
        elif opcao == 2:
            resultado = op1 - op2
        elif opcao == 3:
            resultado = op1 * op2
        elif opcao == 4:
            if op2 != 0:
                resultado = op1 / op2
            else:
                print(f"A divisão não está definida para um divisor = {op2}")
                resultado = "não definido"

        print(f"O resultado da operação é {resultado}")
    else:
        print("Opção inválida")
    