print ("Vamos calcular o volume cubico de uma lata de oleo!")

altura = float(input("Qual a altura da lata? "))
r = float(input("Digite  o valor do raio da circunferencia da lata: "))

quadrado = float(r * r)
volume = float(3.14 * quadrado * altura)

print ("O volume da lata eh: ", volume )