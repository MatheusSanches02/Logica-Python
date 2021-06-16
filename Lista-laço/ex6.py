'''
Faça um programa em Python para controlar o estoque de mercadorias de uma empresa. Inicialmente
o programa deverá preencher duas listas com dez posições cada, onde o primeiro corresponde ao
código do produto e o segundo ao total desse produto em estoque. Logo após, o programa deverá ler um
conjunto "n" de dados contendo o código de um cliente e o código do produto que ele deseja comprar,
juntamente com a quantidade. Código do cliente igual a zero indica que atingiu o limite “n" e o programa
deverá verificar:
- Se o código do produto solicitado existe. Se existir, tentar atender ao pedido; caso contrário, exibir
mensagem Código inexistente;
- Cada pedido feito por um cliente só pode ser atendido integralmente. Caso isso não seja possível,
escrever a mensagem Não temos estoque suficiente desta mercadoria. Se puder atende-lo, escrever a
mensagem Pedido atendido. Obrigado e volte sempre;
- Efetuar a atualização do estoque somente se o pedido for atendido integralmente;
- No final do programa, escrever os códigos dos produtos com seus respectivos estoques já atualizados.
'''

produtos = []
qtdEstoque = []

count = 0

while count < 10: 
    print("Digite o {}º codigo de produto: ".format(count+1))
    cdProduto = int(input("---> "))
    if cdProduto in qtdEstoque:
        print("Produto ja cadastrado!")
    else:
        produtos.append(cdProduto)
        print("Digite a quantidade do produto {} em estoque".format(cdProduto))
        estoque = int(input("---> "))
        while estoque < 0:
            estoque = int(input("Quantidade invalida, digite novamente: "))
        qtdEstoque.append(estoque)
        count += 1


while True:
    print("Entre com o codigo do cliente, digite 0 para finalizar")
    codigo = int(input("---> "))
    if codigo == 0:
        break
    else:
        cdProduto = int(input("Digite o codigo do produto: "))
        if cdProduto in produtos:
            quantidade = int(input("Quantidade que deseja comprar: "))
            posicao = produtos.index(cdProduto)
            if qtdEstoque <= quantidade:
                print("Pedido realizado com sucesso!")
                qtdEstoque = qtdEstoque - quantidade
            else: 
                print("Nao temos estoque suficiente deste produto!")
        else:
            print("Codigo inexistente!")