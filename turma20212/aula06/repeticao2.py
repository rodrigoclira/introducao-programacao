

nome = input("Informe um nome diferente de Rodrigo: ")
while nome.lower() == "rodrigo":
    print("Você informou rodrigo. Mude!")
    nome = input("Informe um nome diferente de Rodrigo: ")

print(nome)
