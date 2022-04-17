palavra = input("Informe a palavra: ")

eh_palidromo = palavra == palavra[::-1]
print(f"A palavra  é palíndroma {eh_palidromo}")