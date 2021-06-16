janela = [0 for i in range(24)]
corredor = [0 for i in range(24)]

while True:
    try: #Tratando exceções
        opcao = int(input("""Digite a opção desejada:
         1  - Vender passagem
         2  - Cancelar compra
         3  - Mostrar mapa de ocupação
         4  - Sair\n>>"""))
    except:
        print("\nOpção inválida, digite novamente.")
        continue
    if opcao == 1:  # Vender Passagem

        if (0 in janela) or (0 in corredor):
            if (0 not in janela):
                print("\nNão temos assentos livres na janela. Opção apenas no corredor.")
                assento = 'C'
            elif (0 not in corredor):
                print("\nNão temos assentos livres no corredor. Opção apenas na janela.")
                assento = 'J'
            else:
                assento = input("Você deseja sentar-se à janela ou ao corredor:  <J>-Janela   <C>-Corredor: ")[0].upper()
                #[0].upper() - Mesmo que a pessoa digite janela (por exemplo) apenas o primeiro caracter será considerado
                while assento not in ["J", "C"]:
                    print("\nTipo de assento inválido")
                    assento = input("Você deseja sentar-se à janela ou ao corredor:  <J>-Janela   <C>-Corredor: ")[0].upper()
            nr_assento = int(input("Digite o número da poltrona que deseja comprar (1-24): "))
            while nr_assento < 1 or nr_assento > 24:
                print("\nNúmero de potrona inválido!")
                nr_assento = int(input("Digite o número da poltrona que deseja comprar (1-24): "))
            if assento == 'J':  # Janela
                if janela[nr_assento - 1] == 1:
                    print("\nPoltrona ocupada. Venda não realizada!!\n")
                else:
                    janela[nr_assento - 1] = 1
                    print("\nVenda realizada com sucesso!!\n")
            else:  # Corredor
                if corredor[nr_assento - 1] == 1:
                    print("\nPoltrona ocupada. Venda não realizada!!\n")
                else:
                    corredor[nr_assento - 1] = 1
                    print("\nVenda realizada com sucesso!!\n")
        else:
            print("\nÔnibus lotado. Opção inválida")

    elif opcao == 2:  # Cancela compra

        if (1 in janela) or (1 in corredor):
            assento = input("Digite o tipo de assento que você deseja cancelar <J>-Janela   <C>-Corredor: ")[0].upper()
            while assento not in ["J", "C"]:  # false
                print("\nTipo de assento inválido")
                assento = input(
                    "Digite o tipo de assento que vocÊ deseja cancelar <J>-Janela   <C>-Corredor: ")[
                    0].upper()

            nr_assento = int(input("Digite o número da poltrona que deseja cancelar (1-24): "))
            while nr_assento < 1 or nr_assento > 24:  # false
                print("\nValor de potrona inválido!")
                nr_assento = int(input("Digite o número da poltrona que deseja cancelar (1-24): "))
            if assento == 'J':  # Janela
                if janela[nr_assento - 1] == 1:
                    janela[nr_assento - 1] = 0
                    print("\nCompra cancelada com sucesso!\n")
                else:
                    print("\nPoltrona livre. Compra não cancelada!")
            else:  # Corredor
                if corredor[nr_assento - 1] == 1:
                    corredor[nr_assento - 1] = 0
                    print("\nCompra cancelada com sucesso!\n")
                else:
                    print("\nPoltrona livre. Compra não cancelada!")
        else:
            print("\nTodas as poltronas estão livres. Opção inválida!")


    elif opcao == 3:  # Mostrar mapa de ocupação

        print("\n.:     Mapa de lugares     :.")
        print("\tJanela\t\t\t  Corredor")

        for i in range(24):
            print(f"{str(i + 1).zfill(2)}-\t{'Ocupada' if (janela[i] == 1) else 'Livre'}\t\t\t" +
                  f"{str(i + 1).zfill(2)}-\t{'Ocupada' if (corredor[i] == 1) else 'Livre'}")
	# zfill() método - preenche uma string numérica com zeros à esquerda, e sabe lidar com sinais positivos e negativos

    elif opcao == 4:  # Sair

        print("\nPrograma finalizado!")
        break

    else:
        print("\nOpção inválida, digite novamente.")
