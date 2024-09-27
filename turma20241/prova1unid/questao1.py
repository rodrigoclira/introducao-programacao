
tabuada = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

print(f"Montando a tabuada de {tabuada} começando em {inicio} e terminando em {fim}:")

valorInicial = inicio
while valorInicial <= fim:
    resultado = tabuada * valorInicial
    print(f"{tabuada} x {valorInicial} = {resultado}")    
    valorInicial+=1