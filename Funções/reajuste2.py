#Invocar função com mais de um parametro

def reajusteSalario(salario, reajuste):
    valorReajustado = salario + (salario * reajuste / 100)
    print(f'Slário reajustado: {valorReajustado}')

salario = float(input("Digite seu salario: "))
percentualReajuste = int(input("Digite o percentual para reajuste: "))

reajusteSalario(salario, percentualReajuste)