
arq = open("texto-escrita.txt", 'a')

#arq.write("Arquivo de Escrita 1\n")
#arq.write("Arquivo de Escrita 2\n")
#arq.write("Arquivo de Escrita 3")

textos = ["Arquivo de Escrita 1\n", "Arquivo de Escrita 2\n", "Arquivo de Escrita 3"]
arq.writelines(textos)

arq.close()