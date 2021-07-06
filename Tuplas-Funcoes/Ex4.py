"""
Faça uma função que recebe uma tupla de números reais e retorna a média aritmética
de todos os valores contidos dentro da tupla .
"""

def mediaTupla(tupla):
    media = sum(tupla) / len(tupla)
    return media