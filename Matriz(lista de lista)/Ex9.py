def preencher_matriz(matriz,tam1,tam2):

    for i in range(tam1):

        linha = []

        for j in range(tam2):
            if(j%2==0): #estou falando das colunas 0,2 e 4
                 linha.append(0)
            else: #estou falando das colunas 1 e 3
                 linha.append(1)

        matriz.append(linha)

    return matriz


def mostrar_matriz(matriz):
    for lista in matriz:
        for elemento in lista:
            print(elemento, end='   ')
        print()


matriz = []


tam1 = 6
tam2 = 5
print("-- Preencher matriz --")

matriz = preencher_matriz(matriz,tam1,tam2)

mostrar_matriz(matriz)