algoritmo "temperatura"
// Fun��o :  Ler uma temperatura em graus Celsius e apresent�-la convertida em
//graus Fahrenheit. A f�rmula de convers�o �: F=(9*C+160) / 5, sendo F a
//temperatura em Fahrenheit e C a temperatura em Celsius.

// Autor :
// Data : 7/24/2019
// Se��o de Declara��es 
var
celsius, fahrenheit: REAL

inicio

ESCREVA("Informe a temperatura em Celsius: ")
LEIA(celsius)

fahrenheit <- (9 * celsius + 160) / 5

ESCREVAL("A temperatura em fahrenheit �", fahrenheit)


fimalgoritmo
