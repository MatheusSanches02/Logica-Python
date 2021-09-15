def ex1():
    lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] 
    listaNegativos = []
    #a)
    maior  = 0
    menor  = 0
    for x in lista:
        if x > maior:
            maior = x
    print(f'O maior numero é o: {maior}')
    #b)
    for i in lista:
        if i < menor:
            menor = i
    print(f'O menor numero é o: {menor}')
    #c)
    for xi in lista:
        if xi % 2  == 0:
            print(f'Numero par: {xi}')
    #d)
    print(f'O numero {lista[0]}, aparece {lista.count(lista[0])} vezes!')
    #e)
    media = sum(lista) / len(lista)
    print(media)
    #f)
    for i  in lista:
        if i < 0:
            listaNegativos.append(i)
    print(f'Os numeros negativos são: {listaNegativos}')

def ex2():
    listaId = []
    listaId.append(input("Digite seu nome: "))
    listaId(input("Digite seu sobrenome: "))
    listaId.append(int(input("Digite su aidade: ")))
    for i in listaId:
        print(i)

def ex3():
    notas = []
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira nota: "))
    nota4 = float(input("Quarta nota: "))
    notas.append(nota1)
    notas.append(nota2)
    notas.append(nota3)
    notas.append(nota4)
    media = sum(notas) / len(notas)
    print(f'A média das suas notas é: {media}')

def ex4():
    dados = dict(nome = input("Digite seu nome: ").title(),
                idade = input("Digite sua idade: "),
                cidade = input("Digite sua cidade").title())
    for chave, valor in dados.items():
        print(chave, ": ", valor)

def ex5():
    continuar = 0
    while continuar == 0:
        dados = dict(nome = input("Digite seu nome: "),
                    idade = input("Digite sua idade: "),
                    cidade = input("Digite sua cidade"))
        continuar = int(input("Deseja continuar? (0 - SIM / 1 - NÃo)"))
        if continuar == 1:
            continuar += 1 
        for chave, valor in dados.items():
            print(chave, ": ", valor)
        
def ex6():
    lista = []
    while len(lista) < 10:
        numero = int(input("Digite um numero inteiro: "))
        if numero not in lista:
            lista.append({"Numero: ": numero})
    print(lista)
    print(f'Foram digitados {len(lista)} numeros diferentes')

def ex7():
    listaA = [9,8,7,1,6,2,4,3,1,6]
    listaB = [8,6,4,9,5,3,1,3,6,4]
    newLista = [listaA, listaB]
    listaC = [listaB]
    for i in listaA:
        if i not in listaB:
            print(f'O numero {i} não aparece na lista B')
    for e in listaA:
        if listaA.count(e) > 1:
            print(f'O numero {e} se repete na lista a')
    for x in listaB:
        if listaB.count(x) > 1:
            print(f'O numero {x} se repete na lista b')
    print(newLista)
    for xi in listaA:
        if xi not in listaB:
            listaC.append(xi)
    print(listaC)

def ex8():
    '''
    mouse = []
    def verifyCode(code): #verifica se o código ja foi cadastrado
        if len(mouse) > 0:
            exist = [x for x in mouse if x["code"] == code]
            if exist:
                return exist[0]
        return
        '''
    def mouseRegister():
        necessitaEsfera = []
        necessitaLimpeza = []
        necessitaCaboConector = []
        quebradoInutilizado = []
        nenhumDefeito = []
        while True:
            code = int(input("Digte o código do mouse: ")) #solicita o código para registro
            if code == 0: #verifica se o código é zero, se sim, sair do programa
                break
            elif code != 0:
                '''
                if verifyCode(code): #chama a função para verificar se o código ja ta cadastrado
                    print("Código já cadastrado!")
                else:
                '''
                print("Opção 1 - Necessita da Esfera") # menu de defeitos
                print("Opção 2 - Necessita de Limpeza ")
                print("Opção 3 - Necessita de troca de cabo ou conector")
                print("Opção 4 - Quebrado ou inutilizado")
                print("Opção 5 - Nenhum defeito")
                defeito = int(input("Selecione o defeito, apenas numero da opção: ")) #pede a opção do defeito ao usuario
                while defeito < 0 or defeito > 5: #válida se a opção digitada existe no menu  
                    print("Opção inválida!")
                    defeito = int(input("Digite uma opção válida: "))
                if defeito == 1: #verifica qual é o defeito e conta no contador do defeito 
                    necessitaEsfera.append(code)
                elif defeito == 2:
                    necessitaLimpeza.append(code)
                elif defeito == 3: 
                    necessitaCaboConector.append(code)
                elif defeito == 4: 
                    quebradoInutilizado.append(code)
                else:
                    nenhumDefeito.append(code)
                #mouse.append({"code": code, "defeito": defeito}) #salva o código do mouse e do defeito em uma lista de dicionário
                print("*--Próximo Mouse--*")

        print("---- Identificação dos mouses sem defeito ----")
        auxiliarNenhumDefeito = sorted(nenhumDefeito)
        print(*auxiliarNenhumDefeito, sep = ',')
        print(f'Total: {len(nenhumDefeito)}')

        print("---- Identificação dos mouses que necessitam de esfera ----")
        auxiliarEsfera = sorted(necessitaEsfera)
        print(*auxiliarEsfera, sep = ',')
        print(f'Total: {len(necessitaEsfera)}')

        print("----Identificação dos mouses que necessitam de limpeza ----")
        auxiliarLimpeza = sorted(necessitaLimpeza)
        print(*auxiliarLimpeza, sep = ',')
        print(f'Total: {len(necessitaLimpeza)}')

        print("---- Identificação dos mouses que necessitam troca de cabo ou conector ----")
        auxiliarCaboConector = sorted(necessitaCaboConector)
        print(*auxiliarCaboConector, sep = ',')
        print(f'Total: {len(necessitaCaboConector)}')

        print("---- Identificação dos mouses que estão quebrados ou inutilizados ----")
        auxiliarQuebrado = sorted(quebradoInutilizado)
        print(*auxiliarQuebrado, sep = ',')
        print(f'Total: {len(quebradoInutilizado)}')
        '''
            percentual1 = (necessitaEsfera / len(mouse)) * 100 #calcula quantos % o defeito representa do total
            percentual2 = (necessitaLimpeza / len(mouse)) * 100
            percentual3 = (necessitaCaboConector / len(mouse)) * 100
            percentual4 = (quebradoInutilizado / len(mouse)) * 100
            print(f'Quantidade de mouses: {len(mouse)}') #imprime a quantidade de mouses cadastrados 
            
        # imprime o final do programa
        print("Situação:                                  Quantidade          Percentual")
        print(f'Necessita de esfera:                             {necessitaEsfera}               {percentual1}%')
        print(f'Necessita de limpeza:                            {necessitaLimpeza}              {percentual2}%')
        print(f'Necessita troca do cabo ou conector:             {necessitaCaboConector}         {percentual3}%')
        print(f'Quebrado ou inutilizado:                         {quebradoInutilizado}           {percentual4}%')
        '''
    mouseRegister()

def menu():
    print("*--Exercicios aula 18--*")
    print("1 - Exercicio 1")
    print("2 - Exercicio 2")
    print("3 - Exercicio 3")
    print("4 - Exercicio 4")
    print("5 - Exercicio 5")
    print("6 - Exercicio 6")
    print("7 - Exercicio 7")
    print("8 - Exercicio 8")
    print("9 - Finalizar programa")
    return int(input("Qual opção desejada: "))

while True:
    op = menu()
    while op < 1 or op > 9:
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
        ex5()
     
    elif op == 6:
        ex6()
    
    elif op == 7:
        ex7()
    elif op == 8:
        ex8()
    else:
        break