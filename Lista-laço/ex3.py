'''
Faça um programa em Python que receba o total de vendas de cada vendedor de uma loja e
armazene-as em uma lista. Receba também o percentual de comissão a que cada vendedor tem direito
e armazene-os em outra lista. Receba os nomes desses vendedores e armazene-os em uma terceira
lista.
Observação: Existem apenas 10 vendedores na loja.
Calcule e mostre:
a) Um relatório com os nomes dos vendedores e os valores a receber referentes á comissão;
b) O total das vendas de todos os vendedores;
c) O maior valor a receber e o nome de quem o receberá;
d) O menor valor a receber e o nome de quem o receberá;
'''

vendas = [] 
vendedores = [] 
comissoes = [] 

vendas_total = 0 
for i in range(10): 
    vendedores.append(input(f"Digite o nome do vendedor {i+1}: ")) 
    vendas.append(float(input(f"Digite o valor vendido pelo vendedor {vendedores[i]}: "))) 

    comissao = float(input(f"Digite o percentual da comissão do vendedor {vendedores[i]}: ")) 
    comissoes.append(vendas[i]*comissao/100) 

for i in len(vendedores): 
    print(f" {vendedores[i]} | {vendas[i]} | R${comissoes[i]:.2f} ") 
    vendas_total += vendas[i] 

print(f"Total de vendas = {vendas_total}") 
print(f"Vendedor com maior valor a receber e sua comissão = {vendedores[comissoes.index(max(comissoes))]} | R${max(comissoes):.2f}") 
print(f"Vendedor com menor valor a receber e sua comissão = {vendedores[comissoes.index(min(comissoes))]} | R${min(comissoes):.2f}")