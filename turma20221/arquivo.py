
arq = open("exemplo.txt", "rt")

#conteudo = arq.read()
#print(conteudo)

linhas = arq.readlines()
for linha in linhas:
    if "ADS" in linha:
        print(f"Encontrei ADS na {linha}")
#print(linhas)

arq.close()


