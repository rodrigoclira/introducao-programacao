agenda = {}

while True:
    print("""\n
1 - Inserir contato 
2 - Editar contato
3 - Remover contato
4 - Listar todos
5 - Sair""")

    opcao = int(input("Informe uma opção: "))

    if opcao == 1:
        print("Inserção de contato")
        nome = input("Informe o nome do contato: ")
        numero = input("Informe o número do contato: ")
        email = input("Informe o email do contato: ")
        
        if nome not in agenda:
            agenda[nome] = {"tel": numero, "email": email }
            print(f"{nome} adicionado com sucesso")
        else:
            print("Para atualizar um contato, use a opção 2")
    elif opcao == 2:
        print("Atualização de contato")
        nome = input("Informe o nome do contato: ")
        numero = input("Informe o número do contato: ")
        email = input("Informe o email do contato: ")

        if nome in agenda:
            agenda[nome] = {"tel": numero, "email": email }
            print(f"{nome} atualizado com sucesso")
        else:
            print("Para inserir um contato, use a opção 1")
    elif opcao == 3:
        print("Remoção de contato")
        nome = input("Informe o nome do contato: ")

        if nome in agenda:
            del agenda[nome]
        else:
            print("Não posso remover uma chave que não existe")
    elif opcao == 4:
        for pos, nome in enumerate(agenda):
            print(f"({pos+1}) {nome} | tel: {agenda[nome]['tel']} | email: {agenda[nome]['email']}")
        
    if opcao == 5:
        break


print("Finalizando programa...")
print(agenda)
          
