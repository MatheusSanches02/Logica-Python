#Faça um programa em Python que mostre na tela as tabuadas do 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10. 
#Observação: Utilizar um ou dois  laços de repetição para realização desse exercício.

lista = [1,2,3,4,5,6,7,8,9,10]
multiplicador = 0

while multiplicador >=0 and multiplicador < 10:
    multiplicador += 1
    print("Tabuado do ", multiplicador)
    if lista[0]:
        print(1 * multiplicador)
        if lista[1]:
            print(2 * multiplicador)
            if lista[2]:
                print(3 * multiplicador)
                if lista[3]:
                    print(4 * multiplicador)
                    if lista[4]:
                        print(5 * multiplicador)
                        if lista[5]:
                            print(6 * multiplicador)
                            if lista[6]:
                                print(7 * multiplicador)
                                if lista[7]:
                                    print(8 * multiplicador)
                                    if lista [8]:    
                                        print(9 * multiplicador)
                                        if lista[9]:
                                            print(10 * multiplicador)
