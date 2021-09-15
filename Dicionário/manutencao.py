def mouseRegister():
    '''
    mouse = []
    def verifyCode(code): #verifica se o código ja foi cadastrado
        if len(mouse) > 0:
            exist = [x for x in mouse if x["code"] == code]
            if exist:
                return exist[0]
        return
    '''
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
