num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outo numero: "))

c = 0


if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux

if num1 % 2 != 0:
    num1+=1

for n in range(num1, num2 + 1):
    if n % 2 != 0:
        c +=1
print("A quantidade de impares entre ", num1 ,"e", num2, "eh: ", c)
