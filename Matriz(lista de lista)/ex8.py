def contar(matriz):
    cont = 0
    for linha in matriz:
        for coluna in linha:
            if coluna == 0:
                cont += 1
    return cont
matriz = [[1,2,0],[0,5,6],[7,8,0]]

print(contar(matriz), "zero(s) encotrado(s)")