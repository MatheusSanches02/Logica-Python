#Faça um programa em Python que receba do usuário sete números inteiros, calcule e mostre:
#a) Os números múltiplos de 2;
#b) Os números múltiplos de 3;

intNumbers = []

for c in range(7):
    intNumbers.append(int(input(f"Digite a posiçao {c} de numero inteiro: ")))

print("--- Multiplo de 2 ---")
for c in range(7):
    if intNumbers[c] % 2 == 0:
        print(intNumbers[c])

print("--- Multiplo de 3 ---")
for c in range(7):
    if intNumbers[c] % 3 == 0:
        print(intNumbers[c])
