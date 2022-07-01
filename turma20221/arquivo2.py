arq = open("exemplo2.txt", "a") #a

arq.write("Olá, ADS\n")
arq.write("IFPE Paulista\n")
arq.write("Introdução a Programação\n")

frases = ["Python\n", "Java\n", "C++\n"]

arq.writelines(frases)
arq.close()
