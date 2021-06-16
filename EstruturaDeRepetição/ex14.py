maior_idade = True
cont = 0
qtde = 100
cont_otimo = soma_ruim = idade_pessimo = 0
cont_pessimo = cont_bom_reg = cont_ruim = 0

while cont < qtde:
    idade = int(input("Digite sua idade: "))
    print(""
    "Notas:\n"
    "A -Ótimo\n"
    "B –Bom\n"
    "C –Regular\n"
    "D –Ruim\n"
    "E -Péssimo")

    resposta = input("Digite sua nota sobre o filme: ").upper()
    if resposta == "A": 
    #a quantidade de respostas Ótimo;
        cont_otimo+=1
    elif resposta == "D": #a média de idade das pessoas que responderam Ruim;
        soma_ruim+=idade #Soma de todas as idades que responderam ruim
        cont_ruim+=1 #Quantidade de pessoas que responderam ruim para conseguir tirar a média
    elif resposta == "E": #quantos % responderam Péssimo e a maior idade que utilizou essa opção;
        if maior_idade: #Significa que é a primeira vez que entra nesse elif
            idade_pessimo = idade 
            maior_idade = False
        else:
            if idade > idade_pessimo:
                idade_pessimo = idade 
                
        cont_pessimo+=1
    elif resposta == "B" or resposta == "C": #a quantidade de respostas Bom e Regular (juntos).
        cont_bom_reg+=1
        cont +=1
print("A quantidade de respostas Ótimo: ",cont_otimo)
print("A média de idade das pessoas que responderam Ruim: ",soma_ruim/cont_ruim if cont_ruim > 0 else "-----")
print("Responderam Péssimo: ",cont_pessimo/qtde*100,"%" )
print("Maior idade dos que responderam Péssimo: ",idade_pessimo if cont_pessimo > 0 else "------")
print("A quantidade de respostas Bom e Regular (juntos): ", cont_bom_reg)