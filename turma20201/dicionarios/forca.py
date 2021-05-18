from random import choice

def forca(sorteada, ofuscada, letra):
    cont=0
    posicoes = []
    while cont < len(sorteada):
        if sorteada[cont] == letra:
            posicoes.append(cont)
        cont+=1

    #print(posicoes)
    lista_ofuscada = list(ofuscada)
    for posicao in posicoes:
        lista_ofuscada[posicao] = letra
    ofuscada = "".join(lista_ofuscada)
    #print(ofuscada)
    return ofuscada

base = {"cor": ["vermelho", "azul", "amarelo"],
        "local": ["brasil", "paulista", "maranguape", "pindamonhangaba"],
        "animal": ["cachorro", "gato", "papagaio"]}

temas = list(base.keys())
print ("Jogo da Forca")
print ("\nTemas disponíveis: ")
print(temas)
tema = input("Informe um tema disponível: ")

if tema not in temas:
    print ("Tema inválido.")
    print ("Programa vai ser finalizado.")
    exit(-1)

palavra_sorteada = choice(base[tema])
#print(palavra_sorteada)
palavra_ofuscada = "_" * len(palavra_sorteada)
print(palavra_ofuscada)
erros = 0
letras_informadas = []

while erros < 7:
    letra = input("\nInforme uma letra: ")
    letra = letra.lower()
    if len(letra) > 1:
        print(f"{letra} é uma letra inválida.")
        print("Tamanho do texto digitado é maior que 1")
        continue

    if letra in letras_informadas:
        print (f"A letra {letra} já foi informada.")
        continue

    letras_informadas.append(letra)

    nova_palavra_ofuscada = forca(palavra_sorteada, palavra_ofuscada, letra)
    #print (nova_palavra_ofuscada)
    if nova_palavra_ofuscada == palavra_ofuscada:
        erros+=1
        print(f"A quantidade de erros atual é {erros}")
    else:
        palavra_ofuscada = nova_palavra_ofuscada

    print(palavra_ofuscada)
    if palavra_ofuscada == palavra_sorteada:
        print("Parabéns, você venceu o jogo")
        break


