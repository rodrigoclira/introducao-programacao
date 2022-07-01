arquivo = open("exemplo2.txt")

for linha in arquivo:
    print(linha, end="")

arquivo.close()