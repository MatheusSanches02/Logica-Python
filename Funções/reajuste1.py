#Invocar funçao sem parametro - sem retorno

def reajustaSalario():
    salario = float(input("Digite seu salário: "))
    valorReajustado = salario * 1.45
    print(f'Salario reajustado: {valorReajustado}')

reajustaSalario()