#operador ternário

kw_m = int(input("Informe o valor do kw por mês: "))
valor_pagar  =  30.0 if kw_m <= 50 and kw_m % 2 == 0 else 30 + (kw_m - 50) * 2.5


print(valor_pagar)

