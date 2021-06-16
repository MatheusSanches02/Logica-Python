cont_par= 2
cont_impar= 1
soma_par= 0
soma_impar= 0
print("---Caro(a) Professor(a), entre com as notas dos alunos ---")
while cont_impar<= 50:
    print("Você está digitando as notas dos alunos ímpares. Por favor, insira a nota do aluno de número ", cont_impar)
    nota = float(input("--> "))
    while nota < 0 or nota > 10:
        print("Você está digitando as notas dos alunos ímpares. Por favor, insira a nota do aluno de número", cont_impar)
        nota = float(input("Nota inválida! Digite novamente!"))
    soma_impar+= nota
    cont_impar+= 2
while cont_par<= 50:
    print("Você está digitando as notas dos alunos pares. Por favor, insira a nota do aluno de número ", cont_par)
    nota = float(input("--> "))
    while nota < 0 or nota > 10:
        print("Você está digitando as notas dos alunos pares. Por favor, insira a nota do aluno de número ",cont_par)
        nota = float(input("Nota inválida! Digite novamente!"))
    soma_par+=nota
    cont_par+=2
media_par= soma_par/ 25
media_impar= soma_impar/ 25
print("Média dos alunos PARES: ",media_par)
print("Média dos alunos ÍMPARES: ",media_impar)
print("A turma que teve maior nota foi a: ", end='')
if media_par> media_impar:
    print("PAR")
elif media_par< media_impar:
    print("ÍMPAR")
else:
    print("As duas turmas (pares e ímpares) tiveram a mesma média")