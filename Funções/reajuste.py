#Invocar a função enviando parametro - com retorno

def reajusteSlaraio(valorSal) :
    valorReajustado = valorSal * 1.45
    return valorReajustado

salario = float(input("Digite o seu salario atual: "))
reajuste = reajusteSlaraio(salario)
print(f'Salario reajustado: {reajuste}')