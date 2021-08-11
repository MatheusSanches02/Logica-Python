lista_nomes = ("Alexandre","João","Carla","Matheus","Mônica")
print(lista_nomes)

print(type(lista_nomes)) #Conseguimos entender o tipo de lista_nomes
#Não é possível acrescentar elementos na tupla
#lista_nomes.append("Catarina")

lista_idades = [] #Aqui sim é uma lista e é mutável
for i in range(len(lista_nomes)): #De 0 até 5
    print("Aluna(o) {} ".format(lista_nomes[i]))
    idade = int(input("Digite a idade: "))
    #if idade < 0:
        #print("Idade inválida")
    #else:
    lista_idades.append(idade)
    #ou
    #lista_idades.append(int(input("Digite a idade: ")))
print("Pessoas com mais de 18 anos: ")
for i in range(len(lista_nomes)):
    if(lista_idades[i]>18):
        print(lista_nomes[i])
print("Quantidade de alunos com 18 anos:  {}".format(lista_idades.count(18)))
print("Menor idade: {}".format(min(lista_idades)))
print("Maior idade: {}".format(max(lista_idades)))
