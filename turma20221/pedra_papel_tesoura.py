def pedra_papel_tesoura(jogador1, jogador2):
    jogo = {"pedra" : {"tesoura": "jogador1",
                       "papel": "jogador2"},
            "papel" : {"tesoura": "jogador2",
                       "pedra" : "jogador1"},
            "tesoura" : {"papel": "jogador1",
                         "pedra": "jogador2"}}
    resultado = ""
    if jogador1 in jogo.keys() and jogador2 in jogo.keys(): 
        if jogador1 == jogador2:
            resultado = "Empate"
        else:
            resultado = jogo[jogador1][jogador2]
    else:
        resltado = "Jogada Inválida"        
        
    return resultado

print(pedra_papel_tesoura("papel", "papel")) #empate
print(pedra_papel_tesoura("tesoura", "pedra")) #jogador2
print(pedra_papel_tesoura("pedra", "tesoura")) #jogador1