secretNumber = int(input("Qual numero pensado? "))
print("~"*30)
print("Adivinhe o numero pensado no inicio do programa")
print("~"*30)


findNumber = 0

cont = 0
while findNumber < secretNumber or findNumber > secretNumber:
    cont = cont + 1
    print("Tentativa numero ", cont)
    findNumber = int(input("-->" ))
    
    if findNumber < secretNumber:
        print("Chutou baixo!")
    elif findNumber > secretNumber:
        print("Chutou alto!")
print("Parabens, você acertou, precisou de ", cont, "tentativas")
