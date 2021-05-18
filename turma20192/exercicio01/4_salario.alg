algoritmo "Salário"
// Função : Escrever um algoritmo que leia o nome de um vendedor, o seu salário
// fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que
//este vendedor ganha 15% de comissão sobre  suas vendas efetuadas, informar o
//seu nome, o salário fixo e salário no final do mês.
// Autor :
// Data : 7/24/2019
// Seção de Declarações 
var
nome: CARACTERE
salario, total_vendas, salario_mes: REAL

inicio
ESCREVA("Informe o nome do vendedor: ")
LEIA(nome)

ESCREVA("Salário de ", nome, ": ")
LEIA(salario)

ESCREVA("Total de vendas efetuadas por ", nome, ": ")
LEIA(total_vendas)

salario_mes <- salario + (total_vendas * 0.15)
ESCREVAL("O vendedor ", nome, " possui um salário fixo de ", salario, " salário com comissão: ", salario_mes)

// Seção de Comandos 
fimalgoritmo
