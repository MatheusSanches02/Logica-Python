# Programa Notas de alunos
# Mostrar a média por aluno envolvendo todas as disciplinas
# O aluno que conseguir a melhor média ganhará uma bolsa de estudos


resposta_continua = 0
notas = {}

disciplinas = ('Computational Thinking using Python','Database Modeling & SQL','Responsive Web Development', 'Agile Software Design', 'AI & Chatbot', 'Domain Driven Design')

while resposta_continua == 0:
    rm = input("Informe o rm do aluno: ")

    if rm in notas.keys():
        print("O rm informado já está na lista. Caso você continue, as notas antigas ({}) serão substituídas.".format(rm))
        rm = input("Informe novamente o nome do aluno (caso informe o mesmo, as notas serão substituídas: ")
    notas = []
    i=0
    soma = 0
    while i < len(disciplinas):
        nota = float(input("Informe a nota deste aluno na disciplina {}: ".format(disciplinas[i])))
        notas.append(nota)
        soma = soma + nota
        i = i+1
    resposta_continua = int(input("Você deseja informar a nota de um novo aluno?(0-SIM / 1-NAO): "))
    if resposta_continua == 1:
        resposta_continua += 1
    notas = {}

media = soma / len(notas)
print("A média da turma é {}".format(media))
print("--- Relatório ---")
for aluno, nota in notas.items:
    print("{} ---- {}".format(aluno,nota))