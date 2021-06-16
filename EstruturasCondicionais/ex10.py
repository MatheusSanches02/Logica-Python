print("Menu de opções:")
print("1 - Somar dois numeros")
print("2 - Raiz quadrada de um numero")
opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    soma = n1 + n2
    print(soma)
else:
    num = float(input("Digite um numero: "))
    raiz = float(num) ** 0.5
    print(raiz)


