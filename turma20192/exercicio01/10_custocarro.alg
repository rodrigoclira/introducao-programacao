algoritmo "Custo do Carro"
// Fun��o : O custo ao consumidor de um carro novo � a soma do custo de  f�brica
//com a percentagem do distribuidor e dos impostos (aplicados, primeiro os impostos
//sobre o custo de f�brica, e depois a percentagem do distribuidor sobre o resultado).
//Supondo que a percentagem do distribuidor seja de 28% e os  impostos 45%. Escrever
//um algoritmo que leia o custo de f�brica de um carro e informe o custo ao consumidor
//do mesmo.
// Autor :
// Data : 7/24/2019
// Se��o de Declara��es 
var
custo_fabrica, custo_final: REAL
inicio

ESCREVA("Informe o custo de f�brica do carro: ")
LEIA(custo_fabrica)

custo_final <- (custo_fabrica + (custo_fabrica * 0.45)) * 1.28

ESCREVAL ("O custo final do carro � ", custo_final)

fimalgoritmo
