realNumbers = []

soma = 0
negativos = 0

for c in range(10):
    realNumbers.append(float(input(f"Digite o valor para a posição {c}: ")))
    if realNumbers[c] < 0:
        negativos += 1
    elif realNumbers[c] > 0:
        soma += realNumbers[c]
print("A quantidade de numeros negativos: ", negativos)
print("Soma dos numeros positivos: ", soma)
