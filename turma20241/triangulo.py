
qtd_linhas = int(input("Quantidade de linhas do triangulo: "))

linha_atual = 1

while linha_atual <= qtd_linhas:
    coluna_final = linha_atual
    coluna_atual = 1
    while coluna_atual <= coluna_final:
        print(f"{coluna_atual} ", end="")
        coluna_atual += 1
    print()
    linha_atual += 1