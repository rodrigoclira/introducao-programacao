# 30 por dia
# X dias
# 8% IRPF
dias = input("Informe a quantidade de dias trabalhados: ")

valor_bruto = dias * 30.0
imposto = 0.08 * valor_bruto  # 8% -> 8/100
valor_liquido = valor_bruto - imposto
print(f"O valor líquido será de R$ {valor_liquido}, imposto R$ {imposto} e valor bruto R$ {valor_bruto}") 