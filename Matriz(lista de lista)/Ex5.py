#Exercicio 5
#Crie um programa em Python que receba do usuário 20 números inteiros.
#Primeiro recebe 20 números inteiros.
#Depois...
#Armazenar os números ordenadamente na matriz 5x4. Mostrar na tela a matriz resultante.
def mostrar_matriz(matriz):
    for lista in matriz:
        for elemento in lista:
            print(elemento, end='   ')
        print()

numeros = [int(input(f"Digite o {n+1}º número: ")) for n in range(0, 20)]
numeros.sort()
matriz = []
inicio = 0
fim = 4
for i in range(0, 5):
    print("Alimentando matriz: ",numeros[inicio:fim] )
    matriz.append(numeros[inicio:fim])
    inicio = fim
    fim += 4

mostrar_matriz(matriz)