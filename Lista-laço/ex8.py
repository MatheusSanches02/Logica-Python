'''
8) Faça um programa em Python que solicite ao usuário 15 números inteiros.
Guardar os números em lista:
A primeira lista deve conter os números positivos e pares.
A segunda lista deve conter os números positivos e ímpares.
A terceira lista deve conter os números negativos.
Validações:
a) Não aceitar número igual a 0 (zero).
b) Não aceitar números repetidos.
c) O usuário precisa digitar obrigatoriamente 15 números válidos conforme validações a e b.
Mostrar na tela:
- As três listas resultantes
- O maior e o menor número digitado pelo usuário
Exemplo:
Lista 1 – números positivos e pares:
Lista 2 – números positivos e ímpares:
Lista 3 – números negativos:
Maior número digitado: 44
Menor número digitado: -9
5 7 3 2 10 2 7 2 5 2
4 8 2 12 44 6 10
5 1 17 13 9
-7 -9 -6
'''

def imprimirNumeros(numeros):
    if len(numeros)>0:
        for num in numeros:
            print(num, end=' ')
    else:
        print("---VAZIO---")

num_pos_pares = []
num_pos_impares = [] 
num_negativos = [] 
numeros = [] 
cont = 0 
numero = 0

while cont<15:
    print("Digite o {}o. numero inteiro: ".format(cont+1))
    numero = int(input("--->"))
    while numero == 0:
        numero = int(input("Numero precisa ser diferente de 0: "))
    if numero not in num_pos_pares and numero not in num_pos_impares and numero not in num_negativos:
        numeros.append(numero)
        if numero > 0:
            if numero % 2 == 0: #par 
                num_pos_pares.append(numero)
            else:
                num_pos_impares.append(numero)
        else:
            num_negativos.append(numero)
        cont+=1
    else:
        print("Numero ",numero," ja existe, digite outro numero")

print("Lista 1 – números positivos e pares:") 
imprimirNumeros(num_pos_pares) 

print("\nLista 2 – números positivos e ímpares:") 
imprimirNumeros(num_pos_impares)

print("\nLista 3 – números negativos:") 
imprimirNumeros(num_negativos) 

print("\n Maior número digitado: ", max(numeros)) 
print("\n Menor número digitado: ", min(numeros))