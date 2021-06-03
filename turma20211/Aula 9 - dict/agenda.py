#Adicionar
#Remover
#Atualizar
#Imprimir todos
#Pesquisar
#Sair

menu="""\n1 - Adicionar contato
2 - Remover contato
3 - Atualizar contato
4 - Imprimir todos contatos
5 - Pesquisar contato
6 - Sair da agenda
Informe a opção: 
"""
agenda = {}
while True:
    op = input(menu)
    if op == '1':
        print("Adicionar contato...")
        nome = input("Nome: ")
        telefone = input("Telefone: ")

        if nome not in agenda:
            agenda[nome] = telefone
        else:
            print(f"O contato {nome} já está na agenda.")
            print(f"Use a opção de atualizar.")
    
    elif op == '3':
        print("Atualizar contato...")
        nome = input("Nome: ")
        telefone = input("Telefone: ")

        if nome in agenda:
            agenda[nome] = telefone
        else:
            print(f"O contato {nome} não está na agenda.")
            print(f"Adicione-o.")
    elif op == '4':
        print("Imprimindo todos contatos")
        #for pos, nome in enumerate(agenda):
        for nome in agenda:
            #print(f'{pos+1:02d} - {nome:15} - {agenda[nome]}')
            print(f'{nome:15} - {agenda[nome]}')
    elif op == '5':
        print("Pesquisando contato")
        nome = input("Nome: ")

        if nome in agenda:
            print(f"{nome} - {agenda[nome]}")
        else:
            print(f"{nome} não está na agenda!")
            
    elif op == "6":
        print ("Saindo da agenda...")
        break

print(agenda)