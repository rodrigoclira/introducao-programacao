
arq = open("texto-escrita.txt")
print(type(arq))

for linha in arq:
    print(linha, end='')
    
arq.close()