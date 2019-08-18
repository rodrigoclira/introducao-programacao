algoritmo "temperatura"
// Função :  Ler uma temperatura em graus Celsius e apresentá-la convertida em
//graus Fahrenheit. A fórmula de conversão é: F=(9*C+160) / 5, sendo F a
//temperatura em Fahrenheit e C a temperatura em Celsius.

// Autor :
// Data : 7/24/2019
// Seção de Declarações 
var
celsius, fahrenheit: REAL

inicio

ESCREVA("Informe a temperatura em Celsius: ")
LEIA(celsius)

fahrenheit <- (9 * celsius + 160) / 5

ESCREVAL("A temperatura em fahrenheit é", fahrenheit)


fimalgoritmo
