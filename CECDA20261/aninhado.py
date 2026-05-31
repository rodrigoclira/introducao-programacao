# teste o códgio aqui

pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f"Resposta da questão {questao}: ")
    if questao == 1 and resposta == "b":
        pontos = pontos + 1
    if questao == 2 and resposta == "a":
        pontos = pontos + 1    
    if questao == 3 and resposta == "d":
        pontos = pontos + 1        
    questao = questao + 1
print(f"O aluno fez {pontos} pontos(s)")  