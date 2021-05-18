algoritmo "notas"
// Função : Escrever um algoritmo que leia o nome de um aluno e as notas das
// três provas que ele obteve no semestre. No final informar o nome do aluno e a
//sua média (aritmética)
// Autor :
// Data : 7/24/2019
// Seção de Declarações 
var
nota1, nota2, nota3, media: REAL
inicio
ESCREVA("Nota 1: ")
LEIA(nota1)

ESCREVA("Nota 2: ")
LEIA(nota2)

ESCREVA("Nota 3: ")
LEIA(nota3)

media <- (nota1+nota2+nota3)/3

ESCREVAL("A Média do aluno é ", media)
fimalgoritmo
