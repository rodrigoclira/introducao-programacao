#
# Lista 
#

# int, float, str, bool  - Tipos simples 
# 1 - Cadastrar
# 2 - Sair

opcao = 1
lista_nomes = []

# append
#
#

while opcao != 5:
    print("Escolha a opção: ")
    print("1 - Cadastrar\n3 - Imprimir todos\n5 - Sair")
    opcao = int(input("Opção escolhida: "))

    if opcao == 1:
        nome = ""
        nome = input("Informe o nome do aluno: ")

        if nome not in lista_nomes:
            lista_nomes.append(nome) # salvar no final da lista
        else:
            print(f"{nome} já está na lista!")
    elif opcao == 3:
        print("\nImprimindo todos os nomes")
        
        # cont = 0
        # while cont < len(lista_nomes):
        #     print(lista_nomes[cont])
        #     cont+=1

        for pos, nome_atual in enumerate(lista_nomes):
             print(f"{pos} - {nome_atual}")

    elif opcao == 5:
        print("Saindo do programa! ")
        break
    else:
        print("Opção inválida! Digite uma opção válida!")

print("Fim do programa!")
print(lista_nomes)