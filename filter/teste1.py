lista = [80, 19, -1, -30, 30, -7, 0, 99, 4, 14, 774, -8, -7]

def maior(num):
    if num >=0:
        return True
    else:
        return False

lista_valida = filter(maior, lista)
print(type(lista_valida))
print(lista_valida)
lista_lista = list(lista_valida)
print(lista_lista)
for i in lista_lista:
    print(i)