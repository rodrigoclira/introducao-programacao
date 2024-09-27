nome_arquivo = "meu-arquivo.txt"
arquivo = open(nome_arquivo, "w")

try:
    while True:
        frase = int(input("Digite uma frase: "))
        if frase == "sair":
            break
        arquivo.write(str(frase) + "\n")
except BaseException as err:
    print(type(err))
    if err is type(ValueError):
        print(f"Erro de valor {err}")

finally:
    print("Fechando o arquivo")
    arquivo.close()
