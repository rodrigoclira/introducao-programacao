valor_inicial = float(input("Valor inicial da dívida: "))
tx_juros = float(input("Taxa de juros: "))
parcela = float(input("Informe o pagamento mensal: "))

if parcela <= valor_inicial * tx_juros: 
    print("Você nunca vai pagar a sua dívida com essa parcela")
    exit(0)

divida = valor_inicial
mes = 0
while divida > 0: 
    divida += divida * tx_juros
    print(f"{mes+1} | Dívida atua: {divida:.2f} | Pagamento mensal R$ {parcela:.2f}")
    divida = divida - parcela
    mes+=1

print(f"Passaram {mes} meses para eu pagar a dívida.")