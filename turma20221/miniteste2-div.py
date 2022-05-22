dividendo = int(input("Informe o dividendo: "))
divisor = int(input("Informe o divisor: "))

resto = dividendo
quociente = 0
while resto >= divisor:
    resto = resto - divisor
    quociente += 1

print(f"O quociente {quociente} e o resto é {resto}")