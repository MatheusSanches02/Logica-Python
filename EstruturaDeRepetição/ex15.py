qtde = int(input("Quantas pessoas participarão do levantamento?: "))
qtde_18 = qtde_menor_18 = qtde_maior_18 = 0
idades = []
for cont in range(qtde):
    idades.append(int(input("Digite sua idade: ")))
    if idades[cont] < 18:
        qtde_menor_18+=1
    elif idades[cont] > 18:
        qtde_maior_18+=1
    else:qtde_18+=1
maior = max(idades)
menor = min(idades)
print("Quantas pessoas possuem 18 anos: ",qtde_18)
print("Quantas pessoas possuem mais de 18 anos: ",qtde_maior_18)
print("Quantas pessoas possuem menos de 18 anos: ",qtde_menor_18)
print("Soma das idades digitadas: ",sum(idades))
print("Média das idades digitadas: ",sum(idades)/qtde)
print("Maior idade {}anos -{} pessoas possuem essa idade".format(maior,idades.count(maior)))
print("Menor idade {}anos -{} pessoas possuem essa idade".format(menor,idades.count(menor)))