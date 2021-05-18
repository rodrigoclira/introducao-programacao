#adicionar
#pesquisar
#remover
agenda = {}

menu = """
Agenda
1 - Adicionar contato
2 - Remover contato
3 - Pesquisar contato
4 - Visualizar toda agenda
5 - Sair
Escolha uma opção (número): 
"""
op = "1"

while True:

    op = input(menu)
    if op == "5":
        break

    if op == "1":
        print ("\nInformações para adição")
        nome = input("Nome: ")
        print ("\nTelefones")
        tel_pessoal = input("Pessoal: ")
        tel_trabalho = input("Trabalho: ")

        if nome not in agenda:
            agenda[nome] = {"PESSOAL": tel_pessoal,
                            "TRABALHO": tel_trabalho}
        else:
            print (f"{nome} já existe na agenda.")
            print ("O contato não foi adicionado.")
    elif op == "2":
        print ("Removendo contato")
        nome = input("Nome a ser removido: ")

        if nome in agenda:
            print(f"{nome} existe na agenda")
            del(agenda[nome]) #removendo contato
            print(f"{nome} removido da agenda")
        else:
            print(f"{nome} não existe na agenda")
        
    elif op == "3":
        print ("Pesquisando contato")
        nome_pesquisado = input("Nome: ")

        valor = agenda.get(nome_pesquisado)
        #print(valor)
        if valor:
            print ("O telefone pessoal é: ")
            print(valor["PESSOAL"])
            print ("O telefone do trabalho é: ")
            print(valor["TRABALHO"])
        else:
            print (f"{nome_pesquisado} não existe na agenda")
    elif op == "4":
        print ("Imprimindo toda a agenda...")
        print (" AGENDA ".center(50,'-'))
        for contato in agenda:
            print ("".center(50,'-'))
            print (contato)
            tel_pessoal = agenda[contato]["PESSOAL"]
            tel_trabalho = agenda[contato]["TRABALHO"]
            print (f"O telefone pessoal é {tel_pessoal} e o telefone do trabalho é {tel_trabalho}.")
    else:
        print ("Opção invalida!")
    
print(agenda)

    
