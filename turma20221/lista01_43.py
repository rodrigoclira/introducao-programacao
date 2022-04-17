# Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# • o total a pagar com desconto de 10%;
# • o valor de cada parcela, no parcelamento de 3× sem juros;
# • a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com des-
# conto)
#• a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

valor_total = float(input("Informe o valor total da compra: "))

total_desconto = valor_total * 0.9
valor_parcela = valor_total / 3
comissao_avista = total_desconto * 0.05 #5/100
comissao_parcelada = valor_total * 0.05

print(f"O valor com desconto de 10% é R$ {total_desconto:.2f}")
print(f"O valor das parcelas em 3 x a prazo é R$ {valor_parcela:.2f}")
print(f"O valor da comissão a vista é R$ {comissao_avista:.2f}")
print(f"O valor da comissão a prazo é R$ {comissao_parcelada:.2f}")