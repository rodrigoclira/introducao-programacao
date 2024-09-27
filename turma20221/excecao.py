
def fetcher(objeto, posicao):
    return objeto[posicao]


x = "spam"


while True:
    try:
        posicao = int(input("Informe a posição: "))
        print(fetcher(x, posicao)) #
    except:
        print("Houve uma exceção")

print("Finalizando programa")
