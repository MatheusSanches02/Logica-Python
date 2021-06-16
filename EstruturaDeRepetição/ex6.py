
unknowTerm = int(input("Qual termo você quer descobrir? "))
firstTerm = 1
secondTerm = 1
cont = 3
if unknowTerm == 1:
    print(1)
elif unknowTerm == 2:
    print(1)
elif unknowTerm > 2:
    while cont <= unknowTerm:
        thirdTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = thirdTerm
        cont += 1
    print(thirdTerm)


  


