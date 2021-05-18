algoritmo "Cotação"
// Função : Elaborar um algoritmo que efetue a apresentação do valor da  conversão
//em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor
//da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.
// Autor :
// Data : 7/24/2019
// Seção de Declarações 
var

conversao, valor_dolar, cotacao: REAL

inicio

ESCREVA("Informe o valor em dólar para conversão: ")
LEIA(valor_dolar)

ESCREVA("Informe a cotação atual do dólar: ")
LEIA(cotacao)

conversao <- valor_dolar / cotacao

ESCREVAL("O valor em real correspondente a ", valor_dolar, " é : ", conversao)

fimalgoritmo
