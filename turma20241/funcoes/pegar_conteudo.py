import glob
from os import path

conteudo = glob.glob("/home/rcls/codigos/git-projects/introducao-programacao/*")
for caminho in conteudo: 
    if path.isfile(caminho):
        print(f"{caminho} é um arquivo")
    elif path.isdir(caminho):
        print(f"{caminho} é uma pasta")
    else:
        print(f"{caminho} não sei do que se trata")

# print(conteudo)