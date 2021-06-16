primeNumber = int(input("Digite um numero: "))

while primeNumber >= 2:
    if primeNumber == 2:
        print("O numero ", primeNumber," é primo")

    elif primeNumber % 2 == 1:
        print("O numero ", primeNumber," é primo")
    else:
        print("O numero ", primeNumber," não é primo!")
    break

