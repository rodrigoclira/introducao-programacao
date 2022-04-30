#Escreva um programa que pergunte o valor
#inicial de uma dívida e o juros mensal.
#Pergunte o valor mensal que será pago.
#Imprima o número de meses para que a dívida
#seja paga, o total pago e o total de juros pago

valor_inicial = float(input("Informe o valor inicial: "))
juros = float(input("Informe o juros: ")) # 2% -> 0.02
#juros_mensal = juros_mensal/100
valor_mensal = float(input("Valor mensal a ser pago: "))

mes = 1
juros_pago = 0

juros_mensal_pago = valor_inicial * juros
divida = valor_inicial + juros_mensal_pago #
divida = divida - valor_mensal
print(f"{mes} - {divida} | {valor_mensal}")
juros_pago += juros_mensal_pago
valor_pago_total = valor_mensal

while divida > 0:
    juros_mensal_pago = divida * juros
    divida = divida + juros_mensal_pago
    juros_pago += juros_mensal_pago

    if divida <= valor_mensal:
        valor_pago_total += divida
        divida = 0
    else:
        divida = divida - valor_mensal
        valor_pago_total += valor_mensal
    
    mes+=1
    print(f"{mes} - {divida} | {valor_mensal}")

print(f"\nValor Pago Total: {valor_pago_total}")
print(f"Juros Pago: {juros_pago}")        
#print(mes)
    