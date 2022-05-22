resultado=0
numero=int(input('DIGITE O NUMERO:'))
if numero==0 or numero==1:
    resultado=1
while numero>=2:
    if resultado==0:
        resultado=numero*(numero-1)
    else :
        resultado=resultado*(numero-1)
    numero=numero-1
print(resultado)
    
    