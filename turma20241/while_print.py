#print(1)
#print(2)
#print(3)
#print(4)
#print(5)
#print(6)
#print(7)
#print(8)
#print(9)
#print(10)

final = int(input("Informe o limite final da impressão: "))
cont = 1

while cont <= final:

    if cont % 2 == 0:        
        print(cont)
    
    cont = cont + 1 # incrementar +1

print("Terminou")