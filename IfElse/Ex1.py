salarioBruto = float(input("Qual o seu salario bruto? R$"))
valorPrestacao = float(input("Qual o valor da presteção? R$"))

limite = salarioBruto * 0.30

aprovacao = valorPrestacao <= limite

if(aprovacao):
    print("Emprestimo concedido!")
else:
    print("Emprestimo não aprovado!")