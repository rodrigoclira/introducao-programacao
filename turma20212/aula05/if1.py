#2.50
VALOR_FIXO = 30.00 # 50 kw 
VALOR_KW = 2.50
VALOR_BASE = 50

kw_mes = int(input("Informe a quantidade de KW do mês: "))

if kw_mes <= VALOR_BASE:
    #print(f"Você vai pagar R$ {VALOR_FIXO:.2f}")
    valor_pagar = VALOR_FIXO 
else:
    print(f"Você gastou muito! Tem pagar a tarifa flexível!")
    excedente = kw_mes - VALOR_BASE
    valor_pagar = VALOR_FIXO + (excedente * VALOR_KW)

print(f"Você vai pagar R$ {valor_pagar:.2f}")
print("Fim do Programa")
