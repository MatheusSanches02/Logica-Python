#Exercício 10
#Faça um programa em Python que preencha uma matriz 7x7 com números inteiros informados pelo usuário.
#Obrigatório o uso de laço de repetição para preencher a matriz.
#Mostrar na tela a  soma dos elementos que estão abaixo da diagonal secundária.
#A soma dos elementos que estão na diagonal secundária.

def soma_abaixo_diagonal(matriz):
    #Diagonal Secundária
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(i+j>=len(matriz)): #Se o exercício pedisse abaixo da diagonal principal seria if(i>j):
                soma+=matriz[i][j]
    return soma