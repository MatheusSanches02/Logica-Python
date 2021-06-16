print("Não atendemos as regiões sul e sudeste")

print("Digite 1 para norte ida, digite 2 para norte ida e volta")
print("Digite 3 para nordeste ida, digite 4 para nordeste ide e volta")
print("Digite 5 para centro-oeste ida e digite 5 para centro-oete ida e volta")

destino = int(input("Para onde você deseja viajar e deseja só ida ou ida e volta? "))

if (destino == 1):
    print("Voce selecionou Norte, o valor da passagem só de ida é R$280,00! Boa Viagem")
elif (destino == 2):
    print("Voce selecionou Norte, o valor da passagem ida e volta é R$400,00! Boa Viagem")
elif (destino == 3):
    print("Voce selecionou Nordeste, o valor da passagem só de ida é R$380,00! Boa Viagem")
elif (destino == 4):
    print("Voce selecionou Nordeste, o valor da passagem de ida e volta é R$628,00! Boa Viagem")
elif (destino == 5):
    print("Voce selecionou Centro-Oeste, o valor da passagem só de ida é R$620,00! Boa Viagem")
elif (destino == 6):
    print("Voce selecionou Centro-Oeste, o valor da passagem de ida e volta é R$1.100,00! Boa Viagem")
else:
    print("Destino não encontrado!")














