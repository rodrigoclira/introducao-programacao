algoritmo "troca valores"
// Função : Ler dois valores para as variáveis A e B, e efetuar as trocas dos
//valores de forma que a variável A passe a possuir o valor da variável B e a
//variável B passe a possuir o valor da variável  A. Apresentar os valores trocados.
// Autor :
// Data : 7/24/2019
// Seção de Declarações 
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
