"""
1) Escreva um programa que simula uma bilheteria de cinema. O operador do programa (usuário do programa) pode deve realizar as seguintes operações:

* Exibir a situação atual da sala de cinema. 
* Mudar o status de uma poltrona, sendo os status possíveis: ocupada, disponível e indisponível.
* Impedir a utilização de uma coluna ou fila (linha) de cadeiras em uma única operação (status = indisponível). A operação será feita por questões de manutenção/distanciamento social. 
* Criar um relatório final de utilização da sala. Com a informação detalhada de cada cadeira e também um resumo de utilização (quantidade de cadeiras ocupadas, disponíveis, e indisponíveis, além da média de ocupação do cinema)

No início é necessário que o operador informe a quantidade de filas (A,B,C.) e a quantidade de colunas (1,2,3…) que a sala do cinema possui. Essa sala deve iniciar sempre vazia.
"""

DESOCUPADO = '0'
OCUPADO = 'X'
INDISPONIVEL = '-'
INVALIDA = '*'

print ("Informe as dimensões do cinema ")
fileiras = int(input("Informe a quantidade de fileiras: "))
cadeiras_fileira = int(input("Informe a quantidade de cadeiras por fileira: "))
cinema = []

# Criando a matriz do cinema
for fileira_pos in range(0, fileiras):
    fileira = []
    for cadeira_pos in range(0, cadeiras_fileira):
        fileira.append(DESOCUPADO)
    cinema.append(fileira)

menu = """
Informe a ação que desejas realizar:
0 - Sair
1 - Imprimir situacão da sala
2 - Mudar a situação de uma cadeira
3 - Impedir a utilização de uma coluna ou fila
4 - Relatório
Opção Escolhida: """

menu_situacao="0 - Desocupado\n1 - Ocupado\n2 - Indisponível: "

while True:
    op = int(input(menu))
    if op == 0:
        break
    elif op == 1:
        print ("\nImprimindo situação das cadeiras\n")
        #imprimindo a informação das colunas
        for cadeira_pos in range(0, cadeiras_fileira):
            print (f"{cadeira_pos:02d}|", end= "") 
        print('')
        
        #Imprindo as cadeiras e os seus identificadores 
        for fileira_pos, fileira in enumerate(cinema):            
            for cadeira_pos, cadeira in enumerate(fileira):
                print(f"{cadeira:3}", end = "")
            print (f"| {fileira_pos:02d}")
            
    elif op == 2:
        fileira_pos = int(input("Fileira: "))
        cadeira_pos = int(input("Cadeira: "))
        print(f"Informe uma opção que deseja inserir na cadeira ({fileira_pos},{cadeira_pos})")
        situacao_cadeira = int(input(menu_situacao))
        
        if situacao_cadeira == 0:
            situacao = DESOCUPADO
        elif situacao_cadeira == 1:
            situacao = OCUPADO
        elif situacao_cadeira == 2:
            situacao = INDISPONIVEL
        else:
            situacao = INVALIDA

        # A cadeira existe na matriz do cinema e a situacao escolhida é valida
        if fileira_pos < fileiras and cadeira_pos < cadeiras_fileira \
                and situacao in [DESOCUPADO, OCUPADO, INDISPONIVEL]:
            cinema[fileira_pos][cadeira_pos] = situacao
        else:
            print("Posição ou situacao de cadeira inválida")
    elif op == 3:
        print ("Opção de bloqueio de fileira/coluna")
        print("Escolha o que você quer bloquear: ")
        opcao_bloqueio = "1 - Fileira\n2 - Coluna: "
        tipo_bloqueio = int(input(opcao_bloqueio))
        
        if tipo_bloqueio == 1:
            fileira_pos = int(input("Informe a fileira: "))
            
            if fileira_pos <  fileiras:
                for cadeira_pos in range(0, cadeiras_fileira):
                    cinema[fileira_pos][cadeira_pos] = INDISPONIVEL
            else:
                print("Fileira escolhida é invalida")
        elif tipo_bloqueio == 2:
            coluna_pos = int(input("Informe a coluna: "))
            
            if coluna_pos <  cadeiras_fileira:
                for fileira_pos in range(0, fileiras):
                    cinema[fileira_pos][coluna_pos] = INDISPONIVEL
            else:
                print("Coluna escolhida é invalida")
    elif op == 4:
        print("Relatório do Cinema")
        tot_ocupada = 0
        tot_desocupada = 0
        tot_indisponivel = 0
        
        for fileira_pos, fileira in enumerate(cinema):
            print (f"Fileira {fileira_pos:02d}")
            for cadeira_pos, cadeira in enumerate(fileira):
                if cadeira == INDISPONIVEL:
                    texto = 'INDISPONÍVEL'
                    tot_indisponivel += 1
                elif cadeira == OCUPADO:
                    texto = 'OCUPADA'
                    tot_ocupada += 1
                elif cadeira == DESOCUPADO:
                    texto = 'DESOCUPADA'
                    tot_desocupada += 1
                print(f"\t({fileira_pos}, {cadeira_pos}): {texto}")
        
        print (f"\bQuantidade de cadeiras ocupadas: {tot_ocupada}")
        print (f"Quantidade de cadeiras desocupadas: {tot_desocupada}")
        print (f"Quantidade de cadeiras indisponíveis: {tot_indisponivel}")
        ocupacao_media = (tot_ocupada / (tot_ocupada + tot_desocupada))*100
        print(f"Média de ocupação: {ocupacao_media:.2f}%")