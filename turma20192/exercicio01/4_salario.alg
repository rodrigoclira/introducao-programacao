algoritmo "Sal�rio"
// Fun��o : Escrever um algoritmo que leia o nome de um vendedor, o seu sal�rio
// fixo e o total de vendas efetuadas por ele no m�s (em dinheiro). Sabendo que
//este vendedor ganha 15% de comiss�o sobre  suas vendas efetuadas, informar o
//seu nome, o sal�rio fixo e sal�rio no final do m�s.
// Autor :
// Data : 7/24/2019
// Se��o de Declara��es 
var
nome: CARACTERE
salario, total_vendas, salario_mes: REAL

inicio
ESCREVA("Informe o nome do vendedor: ")
LEIA(nome)

ESCREVA("Sal�rio de ", nome, ": ")
LEIA(salario)

ESCREVA("Total de vendas efetuadas por ", nome, ": ")
LEIA(total_vendas)

salario_mes <- salario + (total_vendas * 0.15)
ESCREVAL("O vendedor ", nome, " possui um sal�rio fixo de ", salario, " sal�rio com comiss�o: ", salario_mes)

// Se��o de Comandos 
fimalgoritmo
