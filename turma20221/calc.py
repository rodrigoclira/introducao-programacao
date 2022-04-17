menu="""+ | Soma
- | Subtração
* | Multiplicação
/ | Divisão
Escolha: """

op1 = int(input("Informe o operando 1: "))
op2 = int(input("Informe o operando 2: "))
operador = input(menu)

if operador == '+':
    resultado = op1 + op2
elif operador == '-':
    resultado = op1 - op2
elif operador == '*':
    resultado = op1 * op2
elif operador == '/':
    if op2 == 0:
        resultado = None
        mensagem = "Divisão não pode ter divisor=0"
    else:
        resultado = op1 / op2
else:
    mensagem = "Operção diferente de +, /, -, *"
    resultado = None

if resultado != None:
    print(f"{op1} {operador} {op2} = {resultado}")
else:
    print(f"Operação inválida.\n{mensagem}")
    