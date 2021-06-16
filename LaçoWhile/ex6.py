cont = 0
soma = 0

while cont < 50:
    print("Comece a digitar as idades: ")
    idade = int(input("-->"))
    if idade >= 0:
        cont = cont + 1
        soma = idade + soma
    else:
        print("Idade invalida")
    


media = soma/ 50
print("A media das idades eh: ", media)
