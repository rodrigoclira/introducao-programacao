algoritmo "Cota��o"
// Fun��o : Elaborar um algoritmo que efetue a apresenta��o do valor da  convers�o
//em real (R$) de um valor lido em d�lar (US$). O algoritmo dever� solicitar o valor
//da cota��o do d�lar e tamb�m a quantidade de d�lares dispon�veis com o usu�rio.
// Autor :
// Data : 7/24/2019
// Se��o de Declara��es 
var

conversao, valor_dolar, cotacao: REAL

inicio

ESCREVA("Informe o valor em d�lar para convers�o: ")
LEIA(valor_dolar)

ESCREVA("Informe a cota��o atual do d�lar: ")
LEIA(cotacao)

conversao <- valor_dolar / cotacao

ESCREVAL("O valor em real correspondente a ", valor_dolar, " � : ", conversao)

fimalgoritmo
