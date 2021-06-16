'''
Uma escola deseja saber se existem alunos cursando, simultaneamente, as disciplinas Computacional
Thinking using Python e Domain Driven Design.
Coloque os números das matrículas dos alunos que cursam Computacional Thinking using Python em
uma lista.
Coloque os números das matrículas dos alunos que cursam Domain Driven Design em outra lista.
Mostre o número das matrículas que aparecem nas duas listas.
Importante:
Não sabemos quantos alunos estão cursando as disciplinas. Encontre uma solução para que o usuário
digite as matrículas e quando quiser consiga terminar o programa.
'''

studentsCTP = []
studestsDDD = []
studentsAll = []

keepContinue = True
print("Alunos de Computational Thinking Python")
while keepContinue:
    studentsCTP.append(input("Digite o numero de matricula: "))
    keepContinue = input("Digite 'S' para continuar: ").upper()
    if keepContinue != 'S':
        break

keepContinue = True
print("Alunos de Domain Driven Design")
while keepContinue:
    studestsDDD.append(input("Digite o numero de matricula: "))
    keepContinue = input("Digite 'S' para continuar: ").upper()
    if keepContinue != 'S':
        break

for i in range(len(studentsCTP)):
    if studentsCTP[i] in studestsDDD:
        studentsAll.append(studentsCTP[i])

print("Alunos em comum das duas disciplinas")

for registration in studentsAll:
    print(registration)
