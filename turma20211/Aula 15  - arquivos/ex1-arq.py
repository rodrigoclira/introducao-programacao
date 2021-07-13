
#caminho relativo
log = open("arquivo-log.txt", "a")

log.write("IFPE Paulista\n")
log.write("ADS\n")
log.write("Introdução a Programação\n")
log.flush()
texto = ["Elizabeth\n", "Rodrigo\n", "Rosy\n", "Mercio\n", "Alcir\n"]
log.writelines(texto)

log.close()

