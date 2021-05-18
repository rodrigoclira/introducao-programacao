algoritmo "Custo do Carro"
// Função : O custo ao consumidor de um carro novo é a soma do custo de  fábrica
//com a percentagem do distribuidor e dos impostos (aplicados, primeiro os impostos
//sobre o custo de fábrica, e depois a percentagem do distribuidor sobre o resultado).
//Supondo que a percentagem do distribuidor seja de 28% e os  impostos 45%. Escrever
//um algoritmo que leia o custo de fábrica de um carro e informe o custo ao consumidor
//do mesmo.
// Autor :
// Data : 7/24/2019
// Seção de Declarações 
var
custo_fabrica, custo_final: REAL
inicio

ESCREVA("Informe o custo de fábrica do carro: ")
LEIA(custo_fabrica)

custo_final <- (custo_fabrica + (custo_fabrica * 0.45)) * 1.28

ESCREVAL ("O custo final do carro é ", custo_final)

fimalgoritmo
