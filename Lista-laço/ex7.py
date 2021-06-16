''' 
7) Faça um programa em Python que solicite ao usuário 10 números inteiros. Guardar os números em uma lista. Mostrar na tela:
a) Quantos números se repetem. 
b) Quantas vezes eles aparecem. 
Exemplo: 5 7 3 2 10 2 7 2 5 2 Números que aparecem mais de uma vez na lista e quantas vezes aparecem: 5 – 2 vezes 7 – 2 vezes 2 – 4 vezes 
'''

l_num = [] 
numeros = [] #Para guardar apenas os números que aparecem mais de uma vez 
print("Insira 10 números inteiros:") 
for i in range(10): 
    num = int(input("--> ")) 
    l_num.append(num) 
    print("Lista: ",l_num) 
for i in range(len(l_num)): 
    cont = l_num.count(l_num[i]) 
    if cont > 1 and l_num[i] not in numeros: 
        numeros.append(l_num[i]) 
for i in range(len(numeros)): 
            print("{0} - {1} vezes".format(numeros[i], l_num.count(numeros[i])))