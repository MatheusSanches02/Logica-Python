
soma = 0

cont = 1

while cont < 500:
    cont = cont +1
    if (cont %2 != 0 and cont % 3 == 0):
        soma = soma + cont
print("A soma dos impares multiplos de 3 no conjunto de 1 a 500 é: ", soma)
