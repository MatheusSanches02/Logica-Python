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

def ex4():
    
    mouse = []
    def verifyCode(code):
        if len(mouse) > 0:
            exist = [x for x in mouse if x["code"] == code]
            if exist:
                return exist[0]
        return
    def mouseRegister():
        necessitaEsfera = 0
        necessitaLimpeza = 0
        necessitaCaboConector = 0
        quebradoInutilizado = 0
        while True:
            code = int(input("Digte o código do mouse: "))
            if code == 0:
                break
            elif code != 0:
                if verifyCode(code):
                    print("Código já cadastrado!")
                else:
                    print("Opção 1 - Necessita da Esfera")
                    print("Opção 2 - Necessita de Limpeza ")
                    print("Opção 3 - Necessita de troca de cabo ou conector")
                    print("Opção 4 - Quebrado ou inutilizado")
                    defeito = int(input("Selecione o defeito, apenas numero da opção: "))
                    while defeito < 0 or defeito > 4:
                        print("Opção inválida!")
                        defeito = int(input("Digite uma opção válida: "))
                    if defeito == 1:
                        necessitaEsfera = necessitaEsfera + 1
                    elif defeito == 2:
                        necessitaLimpeza = necessitaLimpeza + 1
                    elif defeito == 3: 
                        necessitaCaboConector = necessitaCaboConector + 1
                    else: 
                        quebradoInutilizado = quebradoInutilizado + 1
                    mouse.append({"code": code, "defeito": defeito})
                    print("*--Próximo Mouse--*")
                percentual1 = (necessitaEsfera / len(mouse)) * 100
                percentual2 = (necessitaLimpeza / len(mouse)) * 100
                percentual3 = (necessitaCaboConector / len(mouse)) * 100
                percentual4 = (quebradoInutilizado / len(mouse)) * 100
                print(f'Quantidade de mouses: {len(mouse)}')
        print("Situação:                                  Quantidade          Percentual")
        print(f'Necessita de esfera:                             {necessitaEsfera}               {percentual1}%')
        print(f'Necessita de limpeza:                            {necessitaLimpeza}              {percentual2}%')
        print(f'Necessita troca do cabo ou conector:             {necessitaCaboConector}         {percentual3}%')
        print(f'Quebrado ou inutilizado:                         {quebradoInutilizado}           {percentual4}%')
    mouseRegister()

def menu():
    print("*--Exercicios aula 17--*")
    print("1 - Exercicio 1")
    print("2 - Exercicio 2")
    print("3 - Exercicio 3")
    print("4 - Exercicio 4")
    print("5 - Finalizar Programa")
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
        ex4()
    elif  op == 5:
        break