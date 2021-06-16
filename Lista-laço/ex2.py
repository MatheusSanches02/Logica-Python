#Faça um programa em Python que receba do usuário quinze números inteiros e verifique a existência
#de elementos iguais a 30, mostrando as posições na lista em que apareceram.

intNumbers = []

for c in range(1,16):
    intNumbers.append(int(input(f"Digite o numero da {c}º posição: ")))
    

print(intNumbers.count(30))