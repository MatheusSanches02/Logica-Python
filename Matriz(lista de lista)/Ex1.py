'''
matriz = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

for l in range (0, 7):
    for c in range (0, 2):
        matriz[l][c] = int(input(f'Digite um valor para [{l} , {c}]: '))

print(matriz)
'''


'''
matriz = [[int(input(f"Digite o valor para linha {i} coluna 0: ")), int(input(f"Digite o valor para linha {i} coluna 1: "))] for i in range(7)]
print(f"Quantidade de elementos entre 10 e 20: {len([elemento for lista in matriz for elemento in lista if elemento >=10 and elemento <=20])}")
'''

matriz = []
# Preenchendo a matriz
for i in range(0, 7):
    for c in range(0, 1):
        matriz.append([int(input(f"Digite primeiro número para [{i}][{c}]: ")), int(input(f"Digite segundo número para [{i}][{c+1}]: "))])

print(matriz)

for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()
print(f"Quantidade de elementos entre 10 e 20: {len([elemento for lista in matriz for elemento in lista if elemento >=10 and elemento <=20])}")
