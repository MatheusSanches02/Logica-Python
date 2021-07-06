"""
Crie uma tupla de números inteiros positivos com valores que você quiser, no mínimo
15 valores.
"""

#tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

lista = []

for i in range (0,15):
    numero = int(input("Digite um numero: "))
    lista.append(numero)

tupla = tuple(lista)
