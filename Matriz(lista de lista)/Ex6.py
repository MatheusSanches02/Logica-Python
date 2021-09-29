def preencher_matriz(matriz,tam1,tam2):
    for i in range(tam1):
        linha = []
        for j in range(tam2):
            linha.append(int(input("Entre com um número: ")))
        matriz.append(linha)
    return matriz


def mostrar_matriz(matriz):
    for lista in matriz:
        for elemento in lista:
            print(elemento, end='   ')
        print()


def verificar(ver,primeiro):
    #for i in ver:
    #    if(i!=primeiro):
    #        return False
    #return True
    if all(num == primeiro for num in ver):
        return True
    return False
def ver_quadrado_magico(matriz):
    soma_secundaria = 0
    soma_principal = 0
    soma_linha = []
    soma_coluna = []

    for i in range(len(matriz)):
        total_linha=0
        for j in range(len(matriz)):
            if(i+j==len(matriz)-1):
                soma_secundaria+=matriz[i][j]
            if(i==j):
                soma_principal+=matriz[i][j]
            total_linha+=matriz[i][j]
        soma_linha.append(total_linha)

    for j in range(len(matriz)):
        total_colunas=0
        for i in range(len(matriz)):
            total_colunas+=matriz[i][j]
        soma_coluna.append(total_colunas)

    linha = verificar(soma_linha,soma_linha[0])
    coluna = verificar(soma_coluna,soma_coluna[0])

    print("Soma das linhas: ", soma_linha)
    print("Soma das colunas: ", soma_coluna)
    print("Soma da diagonal principal: ", soma_principal)
    print("Soma da diagonal secundária: ",soma_secundaria)
    if(coluna and linha and soma_principal==soma_secundaria):
        print("É um quadrado mágico")
    else:
        print("Não é um quadrado mágico")

matriz = []

print("Qual o tamanho da matriz? ")
tam1 = 4
tam2 = 4
print("-- Preencher matriz --")
matriz = preencher_matriz(matriz,tam1,tam2)

print("-- Matriz --")
mostrar_matriz(matriz)

ver_quadrado_magico(matriz)