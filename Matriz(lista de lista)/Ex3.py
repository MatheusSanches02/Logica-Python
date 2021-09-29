#Exercicio 3
#Faça um programa em Python que preencha uma matriz 5x5 de números reais.
#Calcule e mostre a soma dos elementos da diagonal secundária.

import random

matriz = [[random.random() for j in range(5)] for i in range(5)]
#matriz = [[float(input(f"Matriz {i}x{j}: ")) for j in range(5)] for i in range(5)]

soma = 0
pos = -1
for linha in matriz:
    print("Linha: ",linha)
    print("--> Somando... :", linha[pos])
    soma += linha[pos]
    pos -= 1
print("Soma da diagonal secundária: ",soma)