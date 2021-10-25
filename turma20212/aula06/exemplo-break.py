# Somar n números. Parar de pedir se for digitado -1

soma = 0
eh_repetir = True
while eh_repetir:
    num = int(input("Informe um número: "))

    if num == -1:
        print("Você solicitou que pare de pedir um número.")
        break
        #eh_repetir = False
    
    soma += num
    # atri
    # mudança

print(f"A soma dos números foi: {soma}")