#adicionar
#remover
#editar
#lista tudo
#procurar nome
menu ="""\nEscolha uma opção:

1 - Adicionar contato
2 - Remover contato
3 - Editar Contato
4 - Procurar Contato
5 - Lista Toda Agenda
6 - Sair

Opção: 
"""
agenda = {}

while True:

    op = int(input(menu))
    print(op)
    if op == 1:
        nome = input("Informe o nome do contato: ")
        numero = input(f"Informe o número de {nome}: ")
        #{"pessoal": ...., "email": ...}
        if nome not in agenda:
            agenda[nome] = numero
            print("Adicionado com sucesso!")
        else:
            print(f"{nome} já existe na agenda. Edite-o.")
    
    elif op == 2:
        nome = input("Informe o nome do contato: ")
        if nome in agenda:
            del agenda[nome]
            print(f"{nome} removido da agenda")
        else:
            print(f"{nome} não está na agenda!")
    elif op == 3:
        nome = input("Informe o nome do contato: ")
        if nome in agenda:
            novo_numero = input("Informe o novo numero: ")
            agenda[nome] = novo_numero
            print(f"numero de {nome} atualizado!")
        else:
            print(f"{nome} não está na agenda!")        
    elif op == 4:
        nome = input("Informe o nome do contato: ")
        if nome in agenda:
            print(f"O {nome} tem o número {numero}")
        else:
            print(f"{nome} não está na agenda!")
    elif op == 5:
        print ("Imprimindo toda a agenda..")
        for pos, nome in enumerate(agenda):
            print(f"{pos} - {nome} - {agenda[nome]}")
            
    if op == 6:
        break
