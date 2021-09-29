matrizA = [[0,0],[0,0]]
matrizB = [[0,0],[0,0]]

for l in range(0,2):
    for c in range(0,2):
        matrizA[l][c] = int(input(f'Digite o valor na posição [{l},{c}]: '))
for l in range(0,2):
    for c in range(0,2):
        matrizB[l][c] = int(input(f'Digite o valor na posição [{l},{c}]: '))

def somarMatrizes(matriz1, matriz2):
    if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
        return None
    result = []
    for i in range(len(matriz1)):   
        result.append([])
        for j in range(len(matriz1[0])):
            result[i].append(matriz1[i][j] + matriz2[i][j])
    return result

soma = somarMatrizes(matrizA, matrizB) # soma e o nosso retorno, result
if soma is not None:
    for i in soma:
        print(i)
else:
    print('Matrizes devem conter o mesmo numero de linhas e colunas')


'''
#Faça um programa em Python que realiza a soma de duas matrizes 2x2.
#Importante: O usuário entrará com os valores (números inteiros) que preencherá
#as duas matrizes (a e b). Mostrar na tela a terceira matriz (c) com a soma de a + b.
def preencher_matriz(matriz): #MatrizA #MatrizB
    for i in range(2):
        linha = []
        for j in range(2):
            linha.append(int(input("Entre com um número: ")))
        matriz.append(linha)
    return matriz

def mostrar_matriz(matrizA,matrizB,matrizC):
     for i in range(len(matrizA)):
        if(i==1):
            print("\n          +            =")
        else:
            print("\n")
        for j in range(len(matrizA)):
          print(matrizA[i][j], end='    ')
        print(end='    ')
        for j in range(len(matrizB)):
          print(matrizB[i][j], end='    ')
        print(end='    ')
        for j in range(len(matrizC)):
          print(matrizC[i][j], end='    ')


matrizA = []
matrizB = []
matrizC = []

print("-- Preencher a matriz A --")
matrizA = preencher_matriz(matrizA)


print("-- Preencher a matriz B --")
matrizB = preencher_matriz(matrizB)

for listaA,listaB in zip(matrizA,matrizB):
    linha = []
    for elementoA, elementoB in zip(listaA,listaB):
        linha.append(elementoA+elementoB)
    matrizC.append(linha)

mostrar_matriz(matrizA,matrizB,matrizC)

'''