tam = 8
matriz = [[int(input(f"Matriz {i}x{j}:  ")) for j in range(tam)] for i in range(tam)]

soma = 0
pos = 0
for linha in matriz:
    soma += linha[pos]
    pos += 1
print("Média da diagonal principal: ",soma/tam)