def verifica_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    if linhas != colunas:
        return False
    for linha in matriz:
        if len(linha) != colunas:
            return False
    return True