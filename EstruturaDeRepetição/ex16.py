
'''
Exercício 16:
Programa: Digitação de notas -Escola JoWell Sant'ana
Manuntenção: 28/04/2021
Descrição da manutenção:
-Acrescentar a digitação dos nomes dos alunos
-Mostrar quantos alunos ficaram com nota abaixo de 6
-Mostrar os nomes dos alunos com nota acima de 9
'''
nomes = [] #28/04/2021
notas = [] #28/04/2021
cont_par = 2
cont_impar = 1
soma_par = 0
soma_impar = 0
qtde=0
print("---Caro(a) Professor(a), entre com as notas dos alunos ---")
while cont_impar <= 10:
    print("Você está digitando as notas dos alunos ímpares. Por favor, insira o nome e a nota do aluno de número ", cont_impar)
    nome = input("Nome --> ") #28/04/2021
    nota = float(input("Nota --> ")) #28/04/2021
    while nota < 0 or nota > 10:
        print("Você está digitando as notas dos alunos ímpares. Por favor, insira a nota do aluno de número ",cont_impar)
        nota = float(input("Nota inválida! Digite novamente!"))
        nomes.append(nome) #28/04/2021
        notas.append(nota) #28/04/2021
        soma_impar += nota
        cont_impar += 2
while cont_par <= 10:
    print("Você está digitando as notas dos alunos pares. Por favor, insira o nome e a nota do aluno de número ",cont_par)
    nome = input("Nome --> ") #28/04/2021
    nota = float(input("Nota --> ")) #28/04/2021
    while nota < 0 or nota > 10:
        print("Você está digitando as notas dos alunos pares. Por favor, insira a nota do aluno de número ",cont_par)
        nota = float(input("Nota inválida! Digite novamente!"))
    nomes.append(nome) #28/04/2021
    notas.append(nota) #28/04/2021
    soma_par+=nota
    cont_par+=2
media_par = soma_par / 25
media_impar = soma_impar / 25
print("Média dos alunos PARES: ",media_par)
print("Média dos alunos ÍMPARES: ",media_impar)
print("A turma que teve maior nota foi a: ", end='')
if media_par > media_impar:
    print("PAR")
elif media_par < media_impar:
    print("ÍMPAR")
else:
    print("As duas turmas (pares e ímpares) tiveram a mesma média")#28/04/2021
    print("---Nomes dos alunos com notas acima de 9 ---")
    for n in range(len(nomes)):
        if notas[n] < 6:
            qtde+=1
        if notas[n] > 9:
            print(nomes[n])
print("Quantidade de alunos com nota abaixo de 6: ",qtde)#28/04/2021