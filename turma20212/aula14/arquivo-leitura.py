
arq = open("texto.txt", 'r')

#texto_todo = arq.read(10)
#print(texto_todo)

linhas = arq.readlines()
print(linhas)
for linha in linhas:
    print(linha)
    
arq.close()