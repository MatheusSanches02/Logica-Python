frutas = ['abacate', 'abacaxi','morango','laranja','amora']

def func_frutas(f):
    return f.startswith('b',1) or f.startswith('m',1)

print(list(filter(func_frutas, frutas)))