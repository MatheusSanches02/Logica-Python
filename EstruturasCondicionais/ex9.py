produto = float(input("Qual o valor do produto? "))

lucro1 = produto * (45 / 100)
lucro2 = produto * (30 / 100)
lucroProduto1 = produto + lucro1
lucroProduto2 = produto + lucro2

if produto <= 20.0:
    print("O valor de venda é: R$", lucroProduto1)
else:
    print("O valor de venda é: R$", lucroProduto2)


