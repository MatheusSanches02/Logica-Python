nome = input("Digite sue nome: ")
nota1 = float(input("Qual sua primeira nota? "))
nota2 = float(input("Qual sua segunda nota? "))
nota3 = float(input("Qual sua terceira nota? "))
faltas = int(input("Quantas faltas você teve? "))
media = (nota1 + nota2 + nota3 ) / 3

limiteFaltas = 80 * 0.25

if media >= 7.0 and faltas <= limiteFaltas:
    print("Parabens ", nome, " você esta aprovado!")
elif media < 7.0:
    print("Reprovado por nota!")
else:
    print("Reprovado por excesso de faltas!")
    

