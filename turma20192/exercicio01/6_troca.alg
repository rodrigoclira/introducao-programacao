algoritmo "troca valores"
// Fun��o : Ler dois valores para as vari�veis A e B, e efetuar as trocas dos
//valores de forma que a vari�vel A passe a possuir o valor da vari�vel B e a
//vari�vel B passe a possuir o valor da vari�vel  A. Apresentar os valores trocados.
// Autor :
// Data : 7/24/2019
// Se��o de Declara��es 
var
a, b, troca: REAL
inicio

ESCREVA("Valor de A: ")
LEIA(a)

ESCREVA("Valor de B: ")
LEIA(b)

troca <- a
a <- b
b <- a

ESCREVAL("Valor de A: ", a, " e valor de B: ", b)


fimalgoritmo
