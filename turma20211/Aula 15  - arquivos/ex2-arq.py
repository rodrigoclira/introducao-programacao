log = open("arquivo-log.txt", "r")

#conteudo1 = log.read(13)
#print(conteudo1)

#conteudo2 = log.read(10)
#print(conteudo2)

#conteudo = log.readlines()
#print(conteudo)

#for linha in log:
#    print(len(linha))

print("Primeiro read")
conteudo = log.read()
print(conteudo)

print("Segundo read")
log.seek(0)
conteudo2 = log.read(14)
print(conteudo2)

log.close()
