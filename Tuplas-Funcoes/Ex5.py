"""
Faça uma função que recebe uma tupla de Strings e retorna a maior String de todos
os valores contidos dentro da tupla .
"""

def maiorStringTupla (tupla):
    maiorString = len(tupla[0])
    maior = tupla[0]
    for nome in tupla:
        if (len(nome)> maiorString):
            maior = nome
            maiorString = len(nome)
    return maior