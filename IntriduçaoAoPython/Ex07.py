print ("Programa para calcular quanto pagarei de juros!")


valorBoleto = float(input("Qual o valor do boleto? R$"))
valorJuros = float(input("Qual a porcentagem de juro? "))
diasAtraso = int(input("Quantos dias de atraso? "))

novoValor = float(valorBoleto  + (valorBoleto * (valorJuros/100))* diasAtraso)

print ("O novo boleto  vale R$", novoValor)