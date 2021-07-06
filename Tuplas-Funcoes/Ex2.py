#Imprima todos os números da tupla anterior na tela, um de cada vez.

"""
tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
for i in tupla:
print(i)
"""

lista = []

for i in range (0,15):
    numero = int(input("Digite um numero: "))
    lista.append(numero)
tupla = tuple(lista)
for i in tupla:
    print(i)
