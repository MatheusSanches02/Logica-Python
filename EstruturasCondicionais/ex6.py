a = float(input("Digite um numero: "))
b = float(input("Digite o segundo numero: "))
c = float(input("Digite mais um numero: "))

if ((b-c) < a < (b+c)) and (( a - c)  < b < (a + c)) and ((a - b) < c < (a + b)):
    if a == b == c:
        print("Triangulo equilatero!")
    elif a != b != c:
        print("Triangulo escaleno!")
    elif a != b == c or a == c != b or b == a != c:
        print("Triangulo isosceles!")
else:
    print("Não da para formar umtriangulo!")

    