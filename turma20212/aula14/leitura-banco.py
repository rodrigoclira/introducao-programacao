
def leitura_banco(nome_arquivo):
    banco_arq = open(nome_arquivo)
    #nossa=3
    banco = {}
    for linha in banco_arq:
        chave, valor = linha.strip().split("=")
        banco[chave] = float(valor)
        print(banco)
    banco_arq.close()
    return banco

if __name__ == '__main__':
    banco = leitura_banco('banco.txt')
    print("O banco final é ")
    print(banco)
    
    