print ("Quanto tempo preciso investir para ter R$1.000.000,00?")

salario = float(input("Qual o seu salario? R$"))
despesas = float(input("Quanto voce gasta por mes? R$"))
resto = float(salario - despesas)
valorAlcancar = 1000000
tempo = float(valorAlcancar / (resto * 12))
print ("Voce tem R$ ", resto, "para investir por mes!")
print ("Voce conseguira R$", valorAlcancar," em ", tempo, " anos!")
