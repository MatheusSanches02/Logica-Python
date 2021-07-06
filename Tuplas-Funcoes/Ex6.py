""" 
Dada uma tupla contendo nomes de Pessoas, escreva um programa que imprime
todas as possíveis duplas que podemos formar com os nomes indicados, por exemplo:
nomes = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia") Seu programa deverá imprimir: Ana
e Bia, Ana e Celi, Ana e Diana, Ana e Eva, Ana e Fabia, Bia e Celi, ....
Sugestão, crie uma função que recebe um nome, uma
tupla e talvez mais um parâmetro.
Sua função imprime na tela todas as possíveis duplas que posso formar com o nome que
foi passado como parâmetro.
"""

def combinaNome (nome, tupla):
    for i in tupla:
        if i == nome or tupla.index(i) < tupla.index(nome):
            continue
        else:
            print(nome + " e " + i)

nomes = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")
for nome in nomes:
    combinaNome(nome, nomes)
    