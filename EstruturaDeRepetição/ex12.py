multiplicationTable = int(input("Qual numero você quer saber a tabuada? "))





if multiplicationTable > 0:
    for i in range(1,11):
        print(i * multiplicationTable)

continuar = int(input("Digite 1 para continuar..."))

while continuar == 1:
    multiplicationTable = int(input("Qual numero você quer saber a tabuada? "))
    if multiplicationTable > 0:
        for i in range(1,11):
            print(i * multiplicationTable)
    continuar = int(input("Digite 1 para continuar..."))

    if continuar != 1:
        print("Programa encerrado!")

