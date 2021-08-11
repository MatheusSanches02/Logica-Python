def ex1():
    students = {'Matheus': 'FIAP', 
                'Guilherme': 'FIAP',
                'Giovanna': 'PUC', 
                'Giovanna': 'FIAP', 
                'Felipe': 'IFMG'}
    print(students.keys())
    print(students.values())

    for nome, colegio in students.items(): # nome se refere a chave e colegio ao valor usando items()
        print('Nome: ', nome) # chave
        print('Colégio: ', colegio) # valor 

def ex2():
    cinema = {'Batman - O cavaleiro das trevas': {
                'Ano': 2008,
                'Ator': 'Christian Bale'
                },
            'Star Wars: Episódio III a vingança dos sith': {
                'Ano':2005,
                'Ator':  'Hayden Christensen'
                }, 
             'Gente Grande': {
                'Ano': 2010,
                'Ator': 'Adam Sandler'
                }, 
             'Vingadores: Ultimato': {
                'Ano':2019,
                'Ator':  'Robert Downey Jr.'
                }, 
             'Invocação do Mal 2': {
                'Ano':2016,
                'Ator':  'Vera Farmiga'
                }}
    for chave, valor in cinema.items():
        print(valor)
        print("Filme: ", chave)
        print("Ano: ", valor['Ano'])
        print("Ator: ", valor["Ator"])

def ex3():
    def situacaoRa(ver_ra):
        dicionario = {8025: "Ativo", 8021: "Ativo", 8022: "Inativo", 8036: "Ativo"}
        return dicionario.get(ver_ra, "RA não encontrado")

    ra = int(input("Digite o RA que deseja pesquisar: "))
    print(situacaoRa(ra))

def menu():
    print("*--Exercicios aula 17--*")
    return int(input("Qual opção desejada: "))
    
while True:
    op = menu()
    while op < 1 or op > 5:
            print("Opção inválida!")
            op = int(input("Digite uma opção valida: "))
    if op == 1: 
        ex1()
    elif op == 2:
        ex2()
    elif op == 3: 
        ex3()
    elif op == 4:
        print("Exercicio 4 ainda nao postado!")
    elif  op == 5:
        break