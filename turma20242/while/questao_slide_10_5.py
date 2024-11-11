tx_juros = float(input("Informe a taxa de juros: "))
deposito = float(input("Deposito Inicial: "))

cont = 1
poupanca = deposito
while cont <= 24:
    ganho = poupanca * tx_juros
    poupanca += ganho
    print(f"{cont}| Ganho= R$ {ganho:.2f} Saldo= R$ {poupanca:.2f}")
    cont+=1

ganho_total =  poupanca - deposito
print(f"O ganho total foi R$ {ganho_total:.2f}")