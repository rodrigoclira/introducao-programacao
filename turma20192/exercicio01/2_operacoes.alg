algoritmo "opera�oes"
// Fun��o : Fa�a um algoritmo que receba dois n�meros e ao final mostre a  soma, subtra��o, multiplica��o e a divis�o dos n�meros lidos.
// Autor :
// Data : 7/24/2019
// Se��o de Declara��es 
var
num1, num2, soma, subtracao, divisao, multiplicacao: REAL
inicio

ESCREVA("N�mero 1: ")
LEIA(num1)

ESCREVA("N�mero 2: ")
LEIA(num2)

soma <- num1 + num2
subtracao <- num1 - num2
divisao <- num1 / num2
multiplicacao <- num1 * num2

ESCREVAL("A soma � ", soma)
ESCREVAL("A subtra��o � ", subtracao)
ESCREVAL("A divis�o � ", divisao)
ESCREVAL("A multiplica��o � ", multiplicacao)

fimalgoritmo
