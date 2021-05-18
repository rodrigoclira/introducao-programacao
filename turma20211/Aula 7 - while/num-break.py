#criar soma de 10 numeros positvos
#se for informado um valor negativo, pare de pedir os valores. 

cont=1
soma = 0
while cont<=10:
    valor = int(input(f"Valor {cont}: "))

    if valor < 0:
        break

    soma += valor  
    cont+=1
   

print(soma)