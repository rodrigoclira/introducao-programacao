#criar soma de 10 numeros positvos
#se for informado um valor negativo, peça novamente um novo valor. 
#from os import system 

cont=1
soma = 0
while cont<=10:
    valor = int(input(f"Valor {cont}: "))
    #system('clear')
    
    if valor >= 0:   
        soma += valor  
        cont+=1

print(soma)