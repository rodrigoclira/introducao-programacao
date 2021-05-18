algoritmo "operaçoes"
// Função : Faça um algoritmo que receba dois números e ao final mostre a  soma, subtração, multiplicação e a divisão dos números lidos.
// Autor :
// Data : 7/24/2019
// Seção de Declarações 
var
num1, num2, soma, subtracao, divisao, multiplicacao: REAL
inicio

ESCREVA("Número 1: ")
LEIA(num1)

ESCREVA("Número 2: ")
LEIA(num2)

soma <- num1 + num2
subtracao <- num1 - num2
divisao <- num1 / num2
multiplicacao <- num1 * num2

ESCREVAL("A soma é ", soma)
ESCREVAL("A subtração é ", subtracao)
ESCREVAL("A divisão é ", divisao)
ESCREVAL("A multiplicação é ", multiplicacao)

fimalgoritmo
